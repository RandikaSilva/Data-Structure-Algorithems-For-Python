from helpers.dictionary_builder import DictionaryBuilder
from helpers.adjacency_builder import AdjacencyMatrixBuilder
from helpers.linkedlist_builder import LinkedListBuilder
from db.database import Database
from constants.environment import _initialize_environment
from server.server import start
import os

class ShortestPath:

    def __init__(self):
        _initialize_environment()
        self.DATA_STRUCTURE_MODE =os.environ.get('DATA_STRUCTURE_MODE')
        self.db = Database()
        self.load_data()

    def load_data(self):
        connected_station_data_set = self.db._get_all_connected_stations()
        station_data_set=self.db._get_all_stations()
        #if self.DATA_STRUCTURE_MODE == "0":
        builder = DictionaryBuilder()
        builder._build(station_data_set,connected_station_data_set)
        #elif self.DATA_STRUCTURE_MODE == "1":
        builder = LinkedListBuilder()
        builder._build(station_data_set,connected_station_data_set)
        #elif self.DATA_STRUCTURE_MODE == "2": 
        # station_count = self.db._get_station_count()[0][0]
        builder = AdjacencyMatrixBuilder()
        builder._build(station_data_set,connected_station_data_set)
        start()

if __name__ == "__main__": 
    ShortestPath() 
