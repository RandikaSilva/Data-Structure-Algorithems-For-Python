class Node:
    def __init__(self, station_name, next_station, distance):
        self.station_name = station_name
        self.distance = distance
        self.next_station = next_station


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, src, next_station, distance):
        if(self.head == None):
            first = Node(src, next_station, distance)
            self.head = first
        else:
            tmp = self.head
            while(tmp.next_station != None):
                tmp = tmp.next_station
            tmp.next_station = Node(src, next_station, distance)

    def get(self, key):
        target_node = None
        temp = self.head
        while temp != None:
            if temp.station_name==key:
                target_node=temp
                break
            temp = temp.next_station
        return target_node

    def pop(self, key):
        target_node = self.head
        target_node_prev = None
        while target_node.station_name != key:
            target_node_prev = target_node
            target_node = target_node.next_station
            if target_node is None:
                break
        if target_node!=None:
            if target_node_prev != None:
                target_node_prev.next_station = target_node.next_station
            else:
                self.head = target_node.next_station

    def get_all(self):
        station_list=[]
        current_station = self.head
        while current_station != None:
            station_list.append({current_station.station_name: current_station.distance})
            current_station = current_station.next_station
        return station_list

    def print(self):
        current_station = self.head
        while current_station != None:
            print(str(current_station.station_name)+":"+str(current_station.distance))
            current_station = current_station.next_station

    def update(self,key,station_name=None,distance=None):
        if station_name is None:
            target_station = self.get(key)
            target_station.distance=distance
        elif distance is None:
            target_station = self.get(key)
            if target_station is not None:
                target_station.station_name=station_name
        elif station_name and distance is not None:
            target_station = self.get(key)
            target_station.distance=distance
            target_station.station_name=station_name

class Graph:
    def __init__(self):
        self.stations = []
        self.stations_arr = []

    def add(self, src, dest, distance):
        if src not in self.stations:
            self.stations_arr.append(SinglyLinkedList())
            self.stations.append(src)
        index = self.stations.index(src)
        self.stations_arr[index].add(dest, None, distance)

    def print_graph(self):
        for i in range(len(self.stations_arr)):
            print(self.stations[i]+"->")
            print(self.stations_arr[i].print())
            print(" \n")
        if len(self.stations_arr) is 0:
            print("Graph empty")

    def get(self, key):
        if key is not None:
            index = self.stations.index(key)
            if index is not None:
                node_list = self.stations_arr[index]
                return node_list.get_all()
        else:
            return []

    def pop(self, key):
        if key is not None:
            index = self.stations.index(key)
            if index is not None:
                self.station_count = self.station_count-1
                self.stations_arr.pop(index)
                self.stations.pop(index)
                self.stations_arr.pop(index)
                for station in self.stations_arr:
                    station.pop(key)
        else:
            self.stations_arr = []

    def update_station_distance(self,src,dest=None,station_name=None,distance=None):
        if src is not None:
            index = self.stations.index(src)
            if index is not None:
                if station_name is None:
                    node_list = self.stations_arr[index]
                    node_list.update(dest,None,distance)
                if dest is None:
                    for station in self.stations_arr:
                        station.update(src,station_name)
                    self.stations[index]=station_name
    
