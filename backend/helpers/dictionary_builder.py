from data.dictionary import DICTIONARY
from db.database import Database
from helpers.station_name_mapper import StationMapper
import uuid as UUID


class DictionaryBuilder:
    def __init__(self):
        self.db = Database()
        self.mapper = StationMapper()

    def _build(self, station_data_set, connected_station_data_set):
        try:
            for data in station_data_set:
                station = data[1]
                DICTIONARY[station] = {}
            for data in connected_station_data_set:
                station = data[0]
                next_station = data[1]
                distance = int(data[2])
                target_data = DICTIONARY.get(station)
                if target_data is not None:
                    DICTIONARY[station][next_station] = distance
                else:
                    DICTIONARY[station] = {next_station: distance}
        except KeyError:
            print("Invalid key")

    def _add_station(self, station):
        try:
            #uuid = str(UUID.uuid4())[:8]
            DICTIONARY[station] = {}
            return
        except KeyError:
            print("Invalid key")
        finally:
            self.db._insert_station_data(station)

    def _add_station_connector(self, station, next_station, distance):
        try:
            #mapped_station_name = self.mapper._convert_to_station_id(station)
            # mapped_next_station_name = self.mapper._convert_to_station_id(
            # next_station)
            # if DICTIONARY[station] is None:
            #     DICTIONARY[mapped_station_name] = {}
            DICTIONARY[station][next_station] = int(
                distance)
            return
        except KeyError:
            print("Invalid key")
        finally:
            self.db._insert_connected_station_data(
                station, next_station, int(distance))

    def _delete(self, key):
        try:
            #mapped_key = self.mapper._convert_to_station_id(key)
            DICTIONARY.pop(key)
            matched_stations = []
            for station in DICTIONARY:
                for connector in DICTIONARY[station]:
                    if connector == key:
                        matched_stations.append(station)
            for station in matched_stations:
                DICTIONARY[station].pop(key)
            return
        except KeyError:
            print("Invalid key")
        finally:
            self.db._delete_station_data(key)

    def _update_station(self, key, station_name):
        try:
            #mapped_key = self.mapper._convert_to_station_id(key)
            # mapped_station_name = self.mapper._convert_to_station_id(
            #     station_name)
            target_data = DICTIONARY[key]
            DICTIONARY[station_name] = target_data
            DICTIONARY.pop(key)
            matched_stations = []
            for station in DICTIONARY:
                for connector in DICTIONARY[station]:
                    if connector == key:
                        matched_stations.append(station)
            print(matched_stations)
            for station in matched_stations:
                target_data = DICTIONARY[station][key]
                DICTIONARY.pop(station)
                DICTIONARY[station] = {}
                DICTIONARY[station][station_name] = target_data
            return
        except KeyError:
            print("Invalid key")
        finally:
            self.db._update_station_data(key, station_name)

    def _update_station_connector(self, station, next_station, distance):
        try:
            #mapped_key = self.mapper._convert_to_station_id(key)
            # mapped_next_station = self.mapper._convert_to_station_id(
            # next_station)
            DICTIONARY[station][next_station] = int(distance)
            return
        except KeyError:
            print("Invalid key")
        finally:
            self.db._update_connected_station_data(
                station, next_station, distance)

    def _get_all(self):
        return DICTIONARY

    def _get(self, key):
        try:
            return DICTIONARY[key]
        except KeyError:
            print("Invalid key")
