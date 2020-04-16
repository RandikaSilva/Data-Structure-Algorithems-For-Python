Djikstra's algorithm pseudocode:
    We need to maintain the path distance of every vertex. We can store that in an array of size v, where v is the number of vertices.

    We also want to able to get the shortest path, not only know the length of the shortest path. For this, we map each vertex to the vertex that last updated its path length.

    Once the algorithm is over, we can backtrack from the destination vertex to the source vertex to find the path.

    A minimum priority queue can be used to efficiently receive the vertex with least path distance.

    function dijkstra(G, S)
        for each vertex V in G
            distance[V] <- infinite
            previous[V] <- NULL
            If V != S, add V to Priority Queue Q
        distance[S] <- 0
        
        while Q IS NOT EMPTY
            U <- Extract MIN from Q
            for each unvisited neighbour V of U
                tempDistance <- distance[U] + edge_weight(U, V)
                if tempDistance < distance[V]
                    distance[V] <- tempDistance
                    previous[V] <- U
        return distance[], previous[]


Tasks:
    (Isuru)
    1)  Load data from the DB at application start & Populate local graph data using that DB data
        - We need to create data structure like below using our DB data
            graph['A'] = {'B': 2, 'C': 4}
            graph['B'] = {'C': 1, 'D': 4, 'E': 2}
            graph['C'] = {'E': 3}
            graph['D'] = {'F': 2}
            graph['E'] = {'D': 3, 'F': 2}
            graph['F'] = {}
        - Use python dictionary (We will discuss that later)
        - https://www.w3schools.com/python/python_dictionaries.asp

    (Nimnadi)
    2)  Whenever user update station data, First we must update our local data cache (Our local data structure)
        - Needed to implement functions for updating,deleting,inserting
        - https://www.w3schools.com/python/python_dictionaries.asp

    (Heshan)
    3) Create database structure to store,
        - All details about train stations

    (Heshan)
    4)  We must only update our remote DB after updating our local data cache (For update,delete,insert) 
        - Functions to communicate with POSTGRESQL database (Select all,Find,Update,Delete,Insert)
        - https://www.postgresql.org/download/

    (Avishka)
    5)  We should implement REST API using python flask framework
        End-points:-
            Request shortest path and distance data (Method-POST,Params-start,destination)
            Update station data (Method-POST,Params-)
            Delete station data (Method-POST,Params-)
            Add new station (Method-POST,Params-)
            Retrive all station data (Method-get,Params-)
        - https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

    (Minoli,Sachini)
    6)  Create attractive UI which include,
        - Update,Delete,Insert forms
        - Form to get starting & ending stations
        - View to represent shortest path
    

Application flow:
    Requesting shortest path:
        Angular app request for shortest path with starting station and ending station -> 
        Server triggers particular function to find shortest path ->
        Send back json respond to angular app

    Updating,Deleting,Inserting:
        Angular app request for update,delete or inserting station ->
        Find changing station in local data cache ->
        Apply the change to the station (Must only manipulate target station) ->
        Do the change to the remote DB ->
        Send back response to angular app

Support:   
    Change global git account:
        git config [--global] user.name "Full Name"
        git config [--global] user.email "email@address.com"

    Install python dependencies:
        pip3 install -r requirements.txt

    Acticate virtual environment:
        py -m venv env
        source env/bin/activate -> MAC
        .\env\Scripts\activate -> WINDOWS

    Push local change to bitbucket:
        git status -> git add . (or git add {file}) -> git push
    
    Pull request:
        git pull

    Common gmail:
        email-pdsadev@gmail.com
        password-pdsadevnibm

https://www.educative.io/edpresso/how-to-implement-a-graph-in-python

8.487701416015625e-05