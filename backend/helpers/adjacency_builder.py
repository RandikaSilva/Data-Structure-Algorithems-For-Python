from adjacency import StoreAdjacencyMatrix
from data_structures.AdjacencyMatrices import AdjacencyMatrix


class AdjacencyMatrixBuilder:
    def __init__(self, data_count):
        storage = StoreAdjacencyMatrix(data_count)
        self.ADJACENCY = storage.ADJACENCY

    def _build(self, data_set):
        for data in data_set:
            station = data.get('station_id')
            next_station = data.get('next_station')
            distance = data.get('distance')
            self.ADJACENCY._add(station, next_station, distance)

    def _add_station(self, station):
        self.ADJACENCY._add_station(station)

    def _add_station_connector(self, station, next_station, distance):
        self.ADJACENCY._add(station,next_station,distance)

    def _delete(self, key):
        self.ADJACENCY._pop(key)

    def _update_station(self, key, station_name):
        self.ADJACENCY._update_station(key,station_name)

    def _update_station_connector(self, key, next_station, distance):   
        self.ADJACENCY._update_station_distance(key,next_station,distance)

    def _get_all(self):
        return self.ADJACENCY.adjacency_matrix

    def _get(self, key):
        return self.ADJACENCY._get(key)
