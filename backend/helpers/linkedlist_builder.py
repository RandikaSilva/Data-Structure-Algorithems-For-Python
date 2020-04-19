from data.linked_list import LINKEDLIST
from db.database import Database
from helpers.station_name_mapper import StationMapper
from data_structures.LinkedList import Graph
import uuid as UUID

class LinkedListBuilder:
    def __init__(self):
        self.db = Database() 
        self.mapper = StationMapper()

    def _build(self, station_data_set, connected_station_data_set):
        for data in station_data_set:
            LINKEDLIST._add_station(data[1])
        for data in connected_station_data_set:
            station = data[0]
            next_station = data[1]
            distance = data[2]
            LINKEDLIST._add(station, next_station, distance)
        #print(data_cache.LINKEDLIST._print_graph())

    def _add_station(self, station):
        try:
            #uuid = str(UUID.uuid4())[:8]
            LINKEDLIST._add_station(station)
            return
        except Exception:
            print(Exception)
        finally:
            self.db._insert_station_data(station)

    def _add_station_connector(self, station, next_station, distance):
        try:
            #mapped_station = self.mapper._convert_to_station_id(station)
            #mapped_next_station = self.mapper._convert_to_station_id(next_station)
            LINKEDLIST._add(station, next_station, int(distance))
            return
        except Exception:
            print(Exception)
        finally:
            self.db._insert_connected_station_data(station, next_station,str(distance))

    def _delete(self, key):
        try:
            #mapped_key = self.mapper._convert_to_station_id(key)
            LINKEDLIST._pop(key)
            return
        except Exception:
            print(Exception)
        finally:
            self.db._delete_station_data(key)

    def _update_station(self, key, station_name):
        try:
            #mapped_key = self.mapper._convert_to_station_id(key)
            #mapped_station_name = self.mapper._convert_to_station_id(station_name)
            LINKEDLIST._update_station_distance(key, None, station_name, None)
            return
        except Exception:
            print(Exception)
        finally:
            self.db._update_station_data(key, station_name)

    def _update_station_connector(self, key, next_station, distance):
        try:
            #mapped_key = self.mapper._convert_to_station_id(key)
            #mapped_next_station = self.mapper._convert_to_station_id(next_station)
            LINKEDLIST._update_station_distance(key, next_station, None, str(distance))
            return
        except Exception:
            print(Exception)
        finally:
            self.db._update_connected_station_data(key, next_station,distance)

    def _get_all(self):
        return LINKEDLIST.stations_arr

    def _get(self, key):
        mapped_key = self.mapper._convert_to_station_id(key)
        return LINKEDLIST._get(mapped_key)
