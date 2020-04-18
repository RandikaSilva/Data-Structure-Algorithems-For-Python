from linked_list import StoreLinkedList

class LinkedListBuilder:
    def __init__(self):
        storage = StoreLinkedList()
        self.LINKED_LIST = storage.LINKED_LIST

    def _build(self, data_set):
            for data in data_set:
                station = data.get('station_id')
                next_station = data.get('next_station')
                distance = data.get('distance')
                self.LINKED_LIST._add(station,next_station,distance)

    def _add_station(self,station):
            self.LINKED_LIST._add_station(station)

    def _add_station_connector(self,station,next_station,distance):
            self.LINKED_LIST._add(station,next_station,distance)
            
    def _delete(self,key):
            self.LINKED_LIST._pop(key)
            
    def _update_station(self,key,station_name):
        self.LINKED_LIST._update_station_distance(key,None,station_name,None)
    
    def _update_station_connector(self,key,next_station,distance):
            self.LINKED_LIST._update_station_distance(key,next_station,None,distance)

    def _get_all(self):
        return self.LINKED_LIST.stations_arr
    
    def _get(self,key):
            return self.LINKED_LIST._get(key)
