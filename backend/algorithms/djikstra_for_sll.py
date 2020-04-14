from linked_list import Graph

class Djikstra:

    # Function which accepts our starting station,destination and our data graph
    def findShortestPath(self, start, destination, graph):# 'A','F'

        # We need to assign infinity value to all nodes expect our starting node. So we can use this contant
        INFINITY = 9999999

        # This list is used to keep track of nodes that we visited
        visited_nodes = {}

        # We need this dictionary to keep shortest distances to all nodes as we go
        shortest_distance = {}

        # This list use to store shortest path from our starting node to destination node after we done
        paths = []

        # We can keep a copy of graph because sometimes data can be updates while running the code. So we can avoid runtime errors
        graph_copy = graph

        # Looping through all element in the graph and setting all nodes to infinity except starting node
        for node in graph_copy.nodes:
            shortest_distance[node] = INFINITY  # Set shortest distance using dictionary. Then we get something like this: {'A':9999999,'B':9999999,'C':9999999} 
        
        shortest_distance[start] = 0 # Then we set starting node distance to Zero

        curr_node = start # Setting current node to starting node

        while graph_copy: # Looping through all the elements until graph_copy has values

            minimum_distance_node = None # Setting minimum distance node to null

            for node in graph_copy.nodes: # Looping through all the elements NODE ='F'
                if(minimum_distance_node == None): #If minimum distance node is null then we are setting minimum_distance_node as first node in our graph
                    minimum_distance_node = node
                elif(shortest_distance[node] < shortest_distance[minimum_distance_node]): # Else we check whether the distance to current node is less than distance to previous minimum distance node.If it is we set minimum distance node to new one
                    minimum_distance_node = node

            if minimum_distance_node is None:
                    break

            path_options = graph_copy.get(minimum_distance_node) # Get all possible paths which is availble in minimum distance node as iterable 

            for i in path_options:
                    for next_node, distance in i.items(): # Unpack path_option array as next_node and distance. Array looks like somthing like this -> [('D',4),('C',2),('E',1)]
                        if next_node and distance is not None:
                            if(shortest_distance[minimum_distance_node]+distance < shortest_distance[next_node]): # Not we are applying Djikstra logic. Here we are checking whether sum of distances of minimum distance node and distance to next node is less than next nodes distance
                                shortest_distance[next_node] = shortest_distance[minimum_distance_node]+distance # if it is, We are updating shortest distance dictionary with new distance
                                visited_nodes[next_node] = minimum_distance_node # And also we are adding visited node to visited_node dictionary
            
            graph_copy.pop(minimum_distance_node) # After, we can remove current node from our graph_copy
       
        # After we iterate through all nodes, now we have our visited_node dictionary
        # Which is something like this {'B': 'A', 'C': 'B', 'D': 'B', 'E': 'B', 'F': 'E'}
        # If you can remember after we apply Djikstra algorithm we come up with table of path to our destination node
        # So first we start from our destination which is F, Then we look for F's value in visited_node then we get value E.
        # Again when we look for E's value we get value B. Just like that when we trace back to our starting node we automatically come up with shortest path
        
        curr_node = destination # Setting current node as destination node
        
        while curr_node != start: # Iterating until we get starting node
            try:
                paths.insert(0, curr_node) # Pushing nodes of our path one by one to paths array
                curr_node = visited_nodes[curr_node] # Change current node to prev node of the path
            except KeyError: # If there is no path to our destination we get KeyError 
                print("Path is not reachable") 
                break

        paths.insert(0, start) # After looping finally we add our starting node because in the loop it breaks when we hit start node (curr_node != start)

        if(shortest_distance[destination] != INFINITY): # Check if distance to our destination node is not equal to infinity
            print("Shortest distance :-     ", shortest_distance[destination]) # Printing shortest distance
            print("Shortest path :-     ", paths) # Printing shortest path


# Represent the graph which holds all possible paths and distances between stations.
# Later on we need to manipulate something like this using our db
# This is a python dictionary. Unlike arrays we can access any data using key values
# For example if I execute graph['A'], it will return this [{'B': 3}, {'C': 4},{'D':7}].
# So we don't need to iterate through all elements in our dataset like in a array to find a value.

g= Graph(6)
g.add_edge('A','B',2)
g.add_edge('A','C',4)

g.add_edge('B','C',1)
g.add_edge('B','D',4)
g.add_edge('B','E',2)

g.add_edge('C','E',3)

g.add_edge('D','F',2)

g.add_edge('E','D',3)
g.add_edge('E','F',2)

g.add_edge('F',None,None)

dj = Djikstra()
dj.findShortestPath('A', 'F', g)
