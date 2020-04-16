class AdjacencyMatrix:
    def __init__(self, station_count):
        self.adjacency_matrix = [[0 for i in range(station_count)]
                    for i in range(station_count)]
        self.stations = []
        self.stations_copy=None
        self.stations_count=station_count

    def add(self, src, dest, distance):
        if dest and distance is not None:
            index_src = None
            index_dest = None
            if src not in self.stations:
                self.stations.append(src)
                index_src = self.stations.index(src)
                self.adjacency_matrix[index_src][index_src] = 0
            else:
                index_src = self.stations.index(src)
            if dest not in self.stations:
                self.stations.append(dest)
                index_dest = self.stations.index(dest)
                self.adjacency_matrix[index_dest][index_dest] = 0
            else:
                index_dest = self.stations.index(dest)

            self.adjacency_matrix[index_src][index_dest]=distance
            self.stations_copy=self.stations.copy()
        else:
            print("Invalid data")
                
    def get(self,key):
        if key is not None and key in self.stations:
                index = self.stations.index(key)
                if index is not None:
                    vertex_list=[] 
                    for i in range(0,self.stations_count):
                        if not i==index and not self.adjacency_matrix[index][i] ==0:
                            vertex_list.insert(0,{self.stations_copy[i]:self.adjacency_matrix[index][i]})
                    return vertex_list
        else:
            return []
            
    def pop(self,key):
        if key in self.stations:
            index = self.stations.index(key)
            self.stations.pop(index)
            self.adjacency_matrix.pop(index)
        else:
            print("Invalid station")

    def update_station_distance(self,src,dest,distance):
        if src and dest in self.stations:
            index_src = self.stations.index(src)
            index_dest = self.stations.index(dest)
            self.adjacency_matrix[index_src][index_dest]=distance
        else:
            print("Invalid station")

    def update_station(self,key,data):
        if key in self.stations:
            index = self.stations.index(key)
            self.stations[index]=data
        else:
            print("Invalid station")