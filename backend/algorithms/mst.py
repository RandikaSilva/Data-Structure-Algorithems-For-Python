from algorithms.djikstra import Djikstra
from constants.errors import ERRORS

class MST:
    def __init__(self):
        self._path = {}
        self._used_nodes = []
        self._undirected_graph = {}
        self._direct_connections = {}

    def _make_undirected_graph(self, graph):
        all_connections = graph._get_all_connections()
        if all_connections['status'] is True:
            for connection in all_connections['data']:
                station_name = connection["station_name"]
                next_station = connection["next_station"]
                distance = connection["distance"]
                if station_name not in self._undirected_graph.keys():
                    self._undirected_graph[station_name] = {}
                    self._undirected_graph[station_name][next_station] = distance
                else:
                    self._undirected_graph[station_name][next_station] = distance
            for connection in all_connections['data']:
                station_name = connection["station_name"]
                next_station = connection["next_station"]
                distance = connection["distance"]
                if next_station not in self._undirected_graph.keys():
                    self._undirected_graph[next_station] = {}
                    self._undirected_graph[next_station][station_name] = distance
                else:
                    self._undirected_graph[next_station][station_name] = distance
        else:
            return ERRORS.get("error")

    def _find_min(self, dictionary):
        min = 9999999
        for key in dictionary:
            if key < min:
                min = key
        return min

    def _get_direct_connections(self, graph, selected_stations):
        all_connections = graph._get_all_connections()
        if all_connections["status"] is True:
            for i in range(len(selected_stations)):
                for station in selected_stations:
                    if selected_stations[i] != station:
                        for connection in all_connections['data']:
                            station_name = connection["station_name"]
                            next_station = connection["next_station"]
                            if station_name == selected_stations[i] and next_station == station:
                                self._direct_connections[station_name] = next_station
        else:
            all_connections="Unable to load direct connections. System error"

    def _get_mst(self, selected_stations, graph):
        self._make_undirected_graph(graph)
        self._get_direct_connections(graph, selected_stations)
        complete = False
        while complete == False:
            if len(self._used_nodes) is 0:
                self._used_nodes.append(selected_stations[0])
            distances = {}
            for used_station in self._used_nodes:
                for checking_station in selected_stations:
                    if used_station != checking_station and checking_station not in self._used_nodes:
                        djikstra = Djikstra(self._undirected_graph)
                        result = djikstra._find_shortest_path(
                            used_station, checking_station)
                        if result['status'] != False:
                            distances[result['data']['distance']
                                      ] = result['data']['shortest_path']
                        else:
                            return {
                                "status": False,
                                "message": "There are invalid stations which is not in the system. Please try again",
                                "data":[]
                            }
            if len(distances) != 0:
                minimum_distances = self._find_min(distances)
                node_data = distances[minimum_distances]
                for index in range(0, len(node_data)-1):
                    try:
                        self._path[node_data[index+1]][node_data[index]]
                    except KeyError:
                        if node_data[index] not in self._path.keys():
                            self._path[node_data[index]] = {}
                            self._path[node_data[index]][node_data[index+1]
                                                         ] = self._undirected_graph[node_data[index]][node_data[index+1]]
                        else:
                            self._path[node_data[index]][node_data[index+1]
                                                         ] = self._undirected_graph[node_data[index]][node_data[index+1]]
                            self._used_nodes.append(node_data[index])
                            self._used_nodes.append(node_data[index+1])
                        if node_data[index] not in self._used_nodes:
                            self._used_nodes.append(node_data[index])
                        if node_data[index+1] not in self._used_nodes:
                            self._used_nodes.append(node_data[index+1])
            matched = 0
            for station in selected_stations:
                if station not in self._used_nodes:
                    continue
                else:
                    matched += 1
            if matched == len(selected_stations):
                break

        total_distance = 0
        final_path = []
        for key in self._path:
            data = self._path[key]
            for data_key in data:
                total_distance += data[data_key]
                final_path.append(str(key)+"->"+str(data_key))
        if len(self._direct_connections) == 0:
            return {
                "status": True,
                "code":101,
                "message": "There no any direct connection between any of your selected stations.So Our system generated shortest path to visit all of your selected stations",
                "data": {
                    "final_path": final_path,
                    "total_distance": total_distance
                }
            }
        else:
            return {
                "status": True,
                "code":100,
                "message": "There are some direct connections between some of your selected stations.If you like you can generate shortest path to visit all of your selected stations else you can only see directed connections between your selected stations",
                "data": {
                    "directed_connections": self._direct_connections,
                    "final_path": final_path,
                    "total_distance": total_distance
                }
        }
