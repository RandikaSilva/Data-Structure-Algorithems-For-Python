from dictionary import StoreDictionary

class DictionaryBuilder:
    def __init__(self):
        storage = StoreDictionary()
        self.DICTIONARY = storage.DICTIONARY

    def _build(self, data_set):
        try:
            for data in data_set:
                station = data.get('station_id')
                next_station = data.get('next_station')
                distance = data.get('distance')
                target_data = self.DICTIONARY.get(station)
                if target_data is not None:
                    self.DICTIONARY[station][next_station]=distance
                else:
                    self.DICTIONARY[station] = {next_station: distance}
            print(self.DICTIONARY)
        except KeyError:
            print("Invalid key")

    def _add_station(self,station):
        try:
            self.DICTIONARY[station]=None
        except KeyError:
            print("Invalid key")

    def _add_station_connector(self,station,next_station,distance):
        try:
            self.DICTIONARY[station][next_station]=distance
        except KeyError:
            print("Invalid key")
            
    def _delete(self,key):
        try:
            self.DICTIONARY.pop(key)
        except KeyError:
            print("Invalid key")
            
    def _update_station(self,key,station_name):
        try:
            target_data = self.DICTIONARY[key]
            self.DICTIONARY[station_name]=target_data
        except KeyError:
            print("Invalid key")
    
    def _update_station_connector(self,key,next_station,distance):
        try:
            self.DICTIONARY[key][next_station]=distance
        except KeyError:   
            print("Invalid key")

    def _get_all(self):
        return self.DICTIONARY
    
    def _get(self,key):
        try:
            return self.DICTIONARY[key]
        except KeyError:
            print("Invalid key")
