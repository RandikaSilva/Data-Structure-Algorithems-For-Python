from db.database import Database
from helpers.station_name_mapper import StationMapper
from constants.errors import ERRORS
import uuid as UUID
import psycopg2
import os
import time

class DictionaryBuilder:
    def __init__(self):
        self.db = Database()
        self.mapper = StationMapper()
        self.DICTIONARY = {}

    def _build(self):
        connected_station_data_set = self.db._get_all_connected_stations()
        station_data_set = self.db._get_all_stations()
        try:
            if connected_station_data_set['status'] and station_data_set['status'] is True:
                for data in station_data_set['data']:
                    station = data[1]
                    self.DICTIONARY[station] = {}
                for data in connected_station_data_set['data']:
                    station = data[0]
                    next_station = data[1]
                    distance = int(data[2])
                    target_data = self.DICTIONARY.get(station)
                    if target_data is not None:
                        self.DICTIONARY[station][next_station] = distance
                    else:
                        self.DICTIONARY[station] = {next_station: distance}
            else:
                return ERRORS.get("database")
        except KeyError:
            return ERRORS.get("key_error")
        except IndexError:
            return ERRORS.get("index")
        except Exception:
            return ERRORS.get("error")

    def _reset_cache_dictionary(self):
        self.DICTIONARY.clear()
        return True

    def _get_cache(self):
        return self.DICTIONARY

    def _add_station(self, station):
        is_error = False
        try:
            start_time = time.time()
            stations = self.DICTIONARY.keys()
            if station not in stations:
                self.DICTIONARY[station] = {}
                print(str(time.time() - start_time)+" Dictionary add station")
                return True
            else:
                is_error = True
                return ERRORS.get("duplicate")
        except KeyError:
            is_error = True
            return ERRORS.get("key_error")
        except Exception:
            is_error = True
            return ERRORS.get("error")
        finally:
            pass
            if is_error == False:
                try:
                    self.db._insert_station_data(station)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _add_station_connector(self, station, next_station, distance):
        is_error = False
        try:
            try:
                start_time = time.time()
                self.DICTIONARY[station][next_station]
                is_error = True
                return ERRORS.get("duplicate")
            except KeyError:
                self.DICTIONARY[station][next_station] = int(distance)
                print(str(time.time() - start_time)+" Dictionary add station connection")
                return True
        except KeyError:
            is_error = True
            return ERRORS.get("key_error")
        except Exception:
            is_error = True
            return ERRORS.get("error")
        finally:
            if is_error == False:
                try:
                    self.db._insert_connected_station_data(
                        station, next_station, int(distance))
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _delete(self, key):
        is_error = False
        try:
            start_time = time.time()
            self.DICTIONARY.pop(key)
            matched_stations = []
            for station in self.DICTIONARY:
                for connector in self.DICTIONARY[station]:
                    if connector == key:
                        matched_stations.append(station)
            for station in matched_stations:
                self.DICTIONARY[station].pop(key)
            print(str(time.time() - start_time)+" Dictionary delete station")
            return True
        except KeyError:
            is_error = True
            return ERRORS.get("key_error")
        except Exception:
            is_error = True
            return ERRORS.get("error")
        finally:
            if is_error == False:
                try:
                    self.db._delete_station_data(key)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _delete_connection(self, key, next_station):
        is_error = False
        try:
            start_time = time.time()
            if self.DICTIONARY[key][next_station] != None:
                self.DICTIONARY[key].pop(next_station)
                print(str(time.time() - start_time)+" Dictionary delete station connection")
                return True
            else:
                return ERRORS.get('not_exist')
        except KeyError:
            is_error = True
            return ERRORS.get("key_error")
        except Exception:
            is_error = True
            return ERRORS.get("error")
        finally:
            if is_error == False:
                try:
                    self.db._delete_station_connection(key, next_station)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _update_station(self, key, station_name):
        is_error = False
        try:
            start_time = time.time()
            target_data = self.DICTIONARY[key]
            self.DICTIONARY[station_name] = target_data
            self.DICTIONARY.pop(key)
            matched_stations = []
            for station in self.DICTIONARY:
                for connector in self.DICTIONARY[station]:
                    if connector == key:
                        matched_stations.append(station)
            for station in matched_stations:
                target_data = self.DICTIONARY[station][key]
                self.DICTIONARY.pop(station)
                self.DICTIONARY[station] = {}
                self.DICTIONARY[station][station_name] = target_data
            print(str(time.time() - start_time)+" Dictionary update station")
            return True
        except KeyError:
            is_error = True
            return ERRORS.get("key_error")
        except Exception:
            is_error = True
            return ERRORS.get("error")
        finally:
            if is_error == False:
                try:
                    self.db._update_station_data(key, station_name)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _update_station_connector(self, station, next_station, distance):
        is_error = False
        try:
            start_time = time.time()
            if self.DICTIONARY[station][next_station] != None:
                self.DICTIONARY[station][next_station] = int(distance)
                print(str(time.time() - start_time)+" Dictionary update station connection")
                return True
            else:
                return ERRORS.get("not_exist")
        except KeyError:
            is_error = True
            return ERRORS.get("key_error")
        except Exception:
            is_error = True
            return ERRORS.get("error")
        finally:
            if is_error == False:
                try:
                    self.db._update_connected_station_data(
                        station, next_station, distance)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _get_all(self):
        start_time = time.time()
        stations = []
        for station in self.DICTIONARY.keys():
            stations.append(station)
        print(str(time.time() - start_time)+" Dictionary get all station")
        return stations

    def _get_all_connections(self):
        start_time = time.time()
        connections = []
        for station_name, connection in self.DICTIONARY.items():
            for next_station, distance in connection.items():
                connections.append({
                    "station_name": station_name,
                    "next_station": next_station,
                    "distance": distance
                })
        if len(connections)!=0:
            print(str(time.time() - start_time)+" Dictionary get all station connections")
            return {
                "status":True,
                "data":connections
            }
        else:
            return ERRORS.get("error")

    def _get(self, key):
        try:
            return self.DICTIONARY[key]
        except KeyError:
            return ERRORS.get("key_error")
