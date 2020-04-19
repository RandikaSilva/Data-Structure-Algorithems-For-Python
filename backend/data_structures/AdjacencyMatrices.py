from constants.errors import ERRORS

class AdjacencyMatrix:
    def __init__(self):
        self.adjacency_matrix = []
        self.stations = []
        self.stations_count=0

    def _add(self, src, dest, distance):
        try:
            if dest and distance is not None:
                index_src = None
                index_dest = None
                if src not in self.stations:
                    self._add_station(src)
                    index_src = self.stations.index(src)
                    self.adjacency_matrix[index_src][index_src] = 0
                else:
                    index_src = self.stations.index(src)
                if dest not in self.stations:
                    self._add_station(dest)
                    index_dest = self.stations.index(dest)
                    self.adjacency_matrix[index_dest][index_dest] = 0
                else:
                    index_dest = self.stations.index(dest)
                if index_src and index_dest is not None: 
                    self.adjacency_matrix[index_src][index_dest]=distance
                    self.stations_copy=self.stations.copy()
                else:
                    return ERRORS.get('not_exist')
            else:
                return ERRORS.get('null_error')
        except KeyError:
            return ERRORS.get('key_error')

    def _add_station(self,station):
        try:
            if station is not None:
                self.stations_count+=1
                self.stations.append(station)
                for station in self.adjacency_matrix:
                    station.append(0)
                self.adjacency_matrix.append([0 for i in range(self.stations_count)])
            else:
                return ERRORS.get('null_error')
        except KeyError:
            return ERRORS.get('key_error')
                
    def _get(self,key):
        try:
            if key is not None and key in self.stations:
                index = self.stations.index(key)
                vertex_list=[] 
                for i in range(0,self.stations_count):
                    if not i==index and not self.adjacency_matrix[index][i] ==0:
                        vertex_list.insert(0,{self.stations_copy[i]:self.adjacency_matrix[index][i]})
                return vertex_list
            else:
                return ERRORS.get('null_error')
        except KeyError:
            return ERRORS.get('key_error')
            
    def _pop(self,key):
        try:
            if key in self.stations:
                index = self.stations.index(key)
                self.stations.pop(index)
                self.adjacency_matrix.pop(index)
                for stations in self.adjacency_matrix:
                    stations.pop(index)
            else:
                return ERRORS.get('not_exist')
        except KeyError:
            return ERRORS.get('key_error')

    def _update_station_distance(self,src,dest,distance):
        try:
            if src and dest in self.stations:
                index_src = self.stations.index(src)
                index_dest = self.stations.index(dest)
                self.adjacency_matrix[index_src][index_dest]=distance
            else:
                return ERRORS.get('not_exist')
        except KeyError:
            return ERRORS.get('key_error')

    def _update_station(self,key,data):
        try:
            if key in self.stations:
                index = self.stations.index(key)
                self.stations[index]=data
            else:
                return ERRORS.get('not_exist')
        except KeyError:
            return ERRORS.get('key_error')
