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
        graph_copy = graph

        for node in graph_copy:
            shortest_distance[node] = INFINITY
        shortest_distance[start] = 0

        curr_node = start

        while graph_copy:

            minimum_distance_node = None
            for node in graph_copy:
                if(minimum_distance_node == None):
                    minimum_distance_node = node
                elif(shortest_distance[node] < shortest_distance[minimum_distance_node]):
                    minimum_distance_node = node
           
            #print(graph_copy)
            path_options = graph_copy[minimum_distance_node].items()

            for next_node, distance in path_options:
                if(shortest_distance[minimum_distance_node]+distance < shortest_distance[next_node]):
                    shortest_distance[next_node] = shortest_distance[minimum_distance_node]+distance
                    visited_nodes[next_node] = minimum_distance_node

            graph_copy.pop(minimum_distance_node)

            curr_node = destination
        while curr_node != start:
            try:
                paths.insert(0, curr_node)
                curr_node = visited_nodes[curr_node]
            except KeyError:
                print("Path is not reachable")
                break
        paths.insert(0, start)

        if(shortest_distance[destination]!=INFINITY):
            print(paths)


# Represent the graph which holds all possible paths and distances between stations.
# Later on we need to manipulate something like this using our db
# This is a python dictionary. Unlike arrays we can access any data using key values
# For example if I execute graph['A'], it will return this [{'B': 3}, {'C': 4},{'D':7}].
# So we don't need to iterate through all elements in our dataset like in a array to find a value.
graph = {}
graph['A'] = {'B': 2, 'C': 4}
graph['B'] = {'C': 1, 'D': 4,'E': 2}
graph['C'] = {'E': 3}
graph['D'] = {'F': 2}
graph['E'] = {'D': 3,'F': 2}
graph['F'] = {}

dj = Djikstra()
dj.findShortestPath('A', 'F', graph)
