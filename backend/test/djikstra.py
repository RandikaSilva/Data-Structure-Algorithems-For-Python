class Djikstra:
    # Function which accepts our starting station,destination and our data graph
    def findShortestPath(self, start, destination, graph):

        # We need to assign infinity value to all nodes expect our starting node. So we can use this contant
        INFINITY = 9999999

        # This list is used to keep track of nodes that we visited
        visited_nodes = {}

        # We want to keep shortest paths to each node.So we use dictionary for that
        shortest_path = {}

        # We need this dictionary to keep shortest distances to all nodes as we go
        shortest_distance = {}

        # This list use to store shortest path from our starting node to destination node after we done
        paths = []

        # We can keep a copy of graph because sometimes data can be updates while running the code. So we can avoid runtime errors
        graph_copy = graph.copy()

        for node in graph_copy:
            shortest_distance[node] = INFINITY
        shortest_distance[start] = 0

        curr_node = start
        
        while graph_copy:
            minimum_distanceNode = None

            for node in graph_copy:
                if(minimum_distanceNode == None):
                    minimum_distanceNode = start
                elif(shortest_distance[node] < shortest_distance[minimum_distanceNode]):
                    minimum_distanceNode = node

            #print(graph_copy.get('A').items())
            path_options = graph_copy.get(minimum_distanceNode)

            for next_node, distance in path_options.items():
                if(shortest_distance[minimum_distanceNode]+distance < shortest_distance[next_node]):
                    shortest_distance[next_node] = shortest_distance[minimum_distanceNode]+distance
                    visited_nodes[next_node] = minimum_distanceNode

            graph_copy.pop(minimum_distanceNode)

        curr_node = destination
        while curr_node != start:
            try:
                paths.insert(0, curr_node)
                curr_node = visited_nodes[curr_node]
            except KeyError:
                print("Path is not reachable")
                break
        paths.insert(0, start)


# Represent the graph which holds all possible paths and distances between stations.
# Later on we need to manipulate something like this using our db
# This is a python dictionary. Unlike arrays we can access any data using key values
# For example if I execute graph['A'], it will return this [{'B': 3}, {'C': 4},{'D':7}].
# So we don't need to iterate through all elements in our dataset like in a array to find a value.
graph = {}
graph['A'] = {'B': 3, 'C': 4, 'D': 7}
graph['B'] = {'C': 1, 'F': 5}
graph['C'] = {'F': 6, 'D': 2}
graph['D'] = {'E': 3, 'G': 6}
graph['E'] = {'G': 3, 'H': 4}
graph['F'] = {'E': 1, 'H': 8}
graph['G'] = {'H': 2}
graph['H'] = {'G': 2}

dj = Djikstra()
dj.findShortestPath('A', 'G', graph)
