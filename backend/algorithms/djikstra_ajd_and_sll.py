class Djikstra:
    def __init__(self, graph):
        self.INFINITY = 9999999
        self.visited_nodes = {}
        self.shortest_distance = {}
        self.paths = []  
        self.graph_copy = graph
        self.checked_nodes={}

    def _find_shortest_path(self, start, destination):  
        for node in self.graph_copy.stations:
            self.shortest_distance[node] = self.INFINITY
        self.shortest_distance[start] = 0
        curr_node = start   
        for i in range(0,len(self.graph_copy.stations)):  
            minimum_distance_node = None  
            for node in self.graph_copy.stations:  
                if self.checked_nodes.get(node)==None:
                    if(minimum_distance_node == None):
                        minimum_distance_node = node
                    elif(self.shortest_distance[node] < self.shortest_distance[minimum_distance_node]):
                        minimum_distance_node = node
            if minimum_distance_node is None:
                break
            path_options = self.graph_copy._get(minimum_distance_node)
            for i in path_options:
                for next_node, distance in i.items():
                    if next_node and distance is not None:
                        if(self.shortest_distance[minimum_distance_node]+distance < self.shortest_distance[next_node]):
                            self.shortest_distance[next_node] = self.shortest_distance[minimum_distance_node]+distance
                            self.visited_nodes[next_node] = minimum_distance_node
            self.checked_nodes[minimum_distance_node]=0
        curr_node = destination 
        while curr_node != start: 
            try:
                self.paths.insert(0, curr_node)
                curr_node = self.visited_nodes[curr_node]
            except KeyError:
                return None

        self.paths.insert(0, start)
        
        if(self.shortest_distance[destination] != self.INFINITY):
           return {
                'distance':self.shortest_distance[destination],
                'shortest_path':self.paths
            }
        else:
            return None
        return None

# graph = Graph()

# graph._add('A', 'B', 2)
# graph._add('A', 'C', 4)

# graph._add('B', 'C', 1)
# graph._add('B', 'D', 4)
# graph._add('B', 'E', 2)

# graph._add('C', 'E', 3)

# graph._add('D', 'F', 2)

# graph._add('E', 'D', 3)
# graph._add('E', 'F', 2)

# graph._add('F', None, None)
# graph._print_graph()
#dj = Djikstra(graph)
#print(dj._find_shortest_path('A', 'F'))