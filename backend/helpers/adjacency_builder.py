from data_structures.AdjacencyMatrices import AdjacencyMatrix
from db.database import Database
from helpers.station_name_mapper import StationMapper
from constants.errors import ERRORS
import uuid as UUID
import psycopg2
import os
import threading

class AdjacencyMatrixBuilder:
    def __init__(self):
        self.db = Database()
        self.mapper = StationMapper()
        self.ADJACENCY = AdjacencyMatrix()

    def _build(self):
        connected_station_data_set = self.db._get_all_connected_stations()
        station_data_set = self.db._get_all_stations()
        try:
            if connected_station_data_set['status'] and station_data_set['status'] is True:
                for data in station_data_set['data']:
                    station = data[1]
                    self.ADJACENCY._add_station(station)
                for data in connected_station_data_set['data']:
                    station = data[0]
                    next_station = data[1]
                    distance = data[2]
                    self.ADJACENCY._add(station, next_station, int(distance))
                os.environ["DATA_MODIFIED"] = "0"
                return True
            else:
                return ERRORS.get("database")
        except IndexError:
            return ERRORS.get("index")
        except Exception:
            return ERRORS.get("error")

    def _get_cache(self):
        return self.ADJACENCY

    def _reset_cache_adjacency(self):
        self.ADJACENCY.adjacency_matrix.clear()
        self.ADJACENCY.stations.clear()
        self.ADJACENCY.stations_count = 0
        return True

    def _add_station(self, station):
        is_error = False
        try:
            result = self.ADJACENCY._add_station(station)
            if result is True:
                return True
            else:
                is_error = True
                return result
        except Exception:
            return ERRORS.get("error")
        finally:
            if is_error == False:
                try:
                    self.db._insert_station_data(station)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _add_station_connector(self, station, next_station, distance):
        is_error = False
        try:
            result = self.ADJACENCY._add(station, next_station, int(distance))
            if result is True:
                return True
            else:
                is_error = True
                return result
        except Exception:
            return ERRORS.get("error")
        finally:
            if is_error == False:
                try:
                    self.db._insert_connected_station_data(
                        station, next_station, distance)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _delete(self, key):
        is_error = False
        try:
            result = self.ADJACENCY._pop(key)
            if result is True:
                return True
            else:
                is_error = True
                return result
        except Exception:
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
            result = self.ADJACENCY._pop_station_connection(key, next_station)
            if result is True:
                return True
            else:
                is_error = True
                return result
        except Exception:
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
            result = self.ADJACENCY._update_station(key, station_name)
            if result is True:
                return True
            else:
                is_error = True
                return result
        except Exception:
            return ERRORS.get("error")
        finally:
            if is_error == False:
                try:
                    self.db._update_station_data(key, station_name)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _update_station_connector(self, key, next_station, distance):
        is_error = False
        try:
            result = self.ADJACENCY._update_station_distance(
                key, next_station, int(distance))
            if result is True:
                return True
            else:
                is_error = True
                return result
        except Exception:
            return ERRORS.get("error")
        finally:
            if is_error == False:
                try:
                    self.db._update_connected_station_data(
                        key, next_station, distance)
                except psycopg2.Error:
                    return ERRORS.get("database")

    def _get_all(self):
        return self.ADJACENCY.stations

    def _get_all_connections(self):
        try:
            connections = []
            for i in range(0, len(self.ADJACENCY.adjacency_matrix)):
                for j in range(0, len(self.ADJACENCY.adjacency_matrix[0])):
                    if self.ADJACENCY.adjacency_matrix[i][j] != 0:
                        connections.append({
                            "station_name": self.ADJACENCY.stations[i],
                            "next_station": self.ADJACENCY.stations[j],
                            "distance": self.ADJACENCY.adjacency_matrix[i][j]
                        })
            return {
                "status": True,
                "data": connections
            }
        except KeyError:
            return ERRORS.get("key_error")
        except Exception:
            return ERRORS.get('error')

    def _get(self, key):
        return self.ADJACENCY._get(key)
