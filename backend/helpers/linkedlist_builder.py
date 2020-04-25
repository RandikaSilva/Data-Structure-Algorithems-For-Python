from db.database import Database
from helpers.station_name_mapper import StationMapper
from data_structures.LinkedList import Graph
from constants.errors import ERRORS
import uuid as UUID
import psycopg2
import os
import time

class LinkedListBuilder:
    def __init__(self):
        self.db = Database() 
        self.mapper = StationMapper()
        self.LINKEDLIST=Graph()

    def _build(self):
        connected_station_data_set = self.db._get_all_connected_stations()
        station_data_set = self.db._get_all_stations()
        try:
            if connected_station_data_set['status'] and station_data_set['status'] is True:
                for data in station_data_set['data']:
                    self.LINKEDLIST._add_station(data[1])
                for data in connected_station_data_set['data']:
                    station = data[0]
                    next_station = data[1]
                    distance = data[2]
                    self.LINKEDLIST._add(station, next_station, distance)
                os.environ["DATA_MODIFIED"]="0"
                return True
            else:
                return ERRORS.get("database")
        except IndexError:
            return ERRORS.get("index")
        except Exception:
            return ERRORS.get("error")

    def _reset_cache_linkedlist(self):
        self.LINKEDLIST.stations_arr.clear()
        self.LINKEDLIST.stations.clear()
        return True

    def _get_cache(self):
        return self.LINKEDLIST

    def _add_station(self, station):
        is_error = False
        try:
            start_time = time.time()
            result = self.LINKEDLIST._add_station(station)
            print(str(time.time() - start_time)+" Linkedlist add station")
            if result is True:
                return True
            else:
                is_error=True
                return result 
        except Exception:
            is_error=True
            return ERRORS.get("error")
        finally:
            if is_error==False:
                try:
                    self.db._insert_station_data(station)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _add_station_connector(self, station, next_stations, distance):
        is_error = False
        try:
            start_time = time.time()
            all_connections = self._get_all_connections()
            for connection in all_connections['data']:
                station_name=connection["station_name"]
                next_station=connection["next_station"]
                if station_name==station and next_station==next_stations:
                    return ERRORS.get("duplicate")
            result = self.LINKEDLIST._add(station, next_stations, int(distance))
            print(str(time.time() - start_time)+" Linkedlist add station connection")
            if result is True:
                return True
            else:
                is_error=True
                return result
        except Exception:
            is_error = True
            return ERRORS.get("error")
        finally:
            if is_error==False:
                try:
                    print(self.db._insert_connected_station_data(station, next_stations,str(distance)))
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _delete(self, key):
        is_error = False
        try:
            start_time = time.time()
            result = self.LINKEDLIST._pop(key)
            print(str(time.time() - start_time)+" Linkedlist delete station")
            if result is True:
                return True
            else:
                is_error=True
                return result
        except Exception:
            is_error=True
            return ERRORS.get("error")
        finally:
            if is_error==False:
                try:
                    self.db._delete_station_data(key)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _delete_connection(self, key,next_station):
        is_error = False
        try:
            start_time = time.time()
            result = self.LINKEDLIST._pop_station_connection(key,next_station)
            print(str(time.time() - start_time)+" Linkedlist delete station connection")
            if result is True:
                return True
            else:
                is_error=True
                return result
        except Exception:
            is_error=True
            return ERRORS.get("error")
        finally:
            if is_error==False:
                try:
                    self.db._delete_station_connection(key,next_station)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _update_station(self, key, station_name):
        is_error = False
        try:
            start_time = time.time()
            result = self.LINKEDLIST._update_station_distance(key, None, station_name, None)
            print(str(time.time() - start_time)+" Linkedlist update station")
            if result is True:
                return True
            else:
                is_error=True
                return result
        except Exception:
            is_error=True
            return ERRORS.get("error")
        finally:
            if is_error==False:
                try:
                    self.db._update_station_data(key, station_name)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _update_station_connector(self, key, next_station, distance):
        is_error = False
        try:
            start_time = time.time()
            result = self.LINKEDLIST._update_station_distance(key, next_station, None, str(distance))
            print(str(time.time() - start_time)+" Linkedlist update station connection")
            if result is True:
                return True
            else:
                is_error=True
                return result
        except Exception:
            is_error=True
            return ERRORS.get("error")
        finally:
            if is_error==False:
                try:
                    self.db._update_connected_station_data(key, next_station,str(distance))
                except psycopg2.Error:
                    return ERRORS.get("database")
 
    def _get_all(self):
        start_time = time.time()
        stations = self.LINKEDLIST.stations
        print(str(time.time() - start_time)+" Linkedlist get all station")
        return stations

    def _get_all_connections(self):
        try:
            start_time = time.time()
            result = self.LINKEDLIST._get_all()
            print(str(time.time() - start_time)+" Linkedlist get all station connections")
            return result
        except Exception:
            return ERRORS.get("error")

    def _get(self, key):
        return self.LINKEDLIST._get(key)
