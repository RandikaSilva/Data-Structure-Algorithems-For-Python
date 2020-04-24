from constants.errors import ERRORS
class Djikstra:
    def __init__(self, graph):
        self.INFINITY = 9999999
        self.visited_nodes = {}
        self.shortest_distance = {}
        self.paths = []  
        self.graph_copy = graph
        self.checked_nodes={}

    def _find_shortest_path(self, start, destination):
        if start and destination is not None:
            try:
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
                if len(self.visited_nodes) !=0 :
                    while curr_node != start: 
                        self.paths.insert(0, curr_node)
                        curr_node = self.visited_nodes[curr_node]
                    self.paths.insert(0, start)
                    if(self.shortest_distance[destination] != self.INFINITY):
                        return {
                        'status':True,
                        'data':{
                            'distance':self.shortest_distance[destination],
                            'shortest_path':self.paths
                        }
                    }
                    else:
                        return ERRORS.get("path_not_exist")
                else:
                    return ERRORS.get("path_not_exist")
            except IndexError:
                return ERRORS.get("index")
            except KeyError: 
                return ERRORS.get("key_error")
            except ArithmeticError: 
                return ERRORS.get("data_type")
        else:
            return ERRORS.get("null_error")