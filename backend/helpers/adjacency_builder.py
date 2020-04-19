from data.adjacency import ADJACENCY
from data_structures.AdjacencyMatrices import AdjacencyMatrix
from db.database import Database
from helpers.station_name_mapper import StationMapper
import uuid as UUID


class AdjacencyMatrixBuilder:
    def __init__(self):
        self.db = Database()
        self.mapper = StationMapper()

    def _build(self, station_data_set, connected_station_data_set):
        for data in connected_station_data_set:
            station = data[0]
            next_station = data[1]
            distance = data[2]
            ADJACENCY._add(station, next_station, int(distance))
        print(ADJACENCY.adjacency_matrix)

    def _add_station(self, station):
        try:
            #uuid = str(UUID.uuid4())[:8]
            ADJACENCY._add_station(station)
        except Exception:
            print(Exception)
        finally:
            self.db._insert_station_data(station)

    def _add_station_connector(self, station, next_station, distance):
        try:
            #mapped_station = self.mapper._convert_to_station_id(station)
            #mapped_next_station = self.mapper._convert_to_station_id(next_station)
            ADJACENCY._add(station, next_station, int(distance))
        except Exception:
            print(Exception)
        finally:
            self.db._insert_connected_station_data(station, next_station, distance)

    def _delete(self, key):
        try:
            #mapped_key = self.mapper._convert_to_station_id(key)
            ADJACENCY._pop(key)
        except Exception:
            print(Exception)
        finally:
            self.db._delete_station_data(key)

    def _update_station(self, key, station_name):
        try:
            #mapped_key = self.mapper._convert_to_station_id(key)
            #mapped_station_name = self.mapper._convert_to_station_id(station_name)
            ADJACENCY._update_station(key, station_name)
        except Exception:
            print(Exception)
        finally:
            self.db._update_station_data(key, station_name)

    def _update_station_connector(self, key, next_station, distance):
        try:
            #mapped_key = self.mapper._convert_to_station_id(key)
            #mapped_next_station = self.mapper._convert_to_station_id(next_station)
            ADJACENCY._update_station_distance(
                key, next_station, int(distance))
        except Exception:
            print(Exception)
        finally:
            self.db._update_connected_station_data(
                key, next_station,distance)

    def _get_all(self):
        return ADJACENCY.adjacency_matrix

    def _get(self, key):
        return ADJACENCY._get(key)
