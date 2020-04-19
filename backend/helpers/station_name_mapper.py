from db.database import Database

class StationMapper:
    def __init__(self):
        self.db = Database()

    def _convert_to_station_name(self,station_id):
        result = self.db._get_station_by_id(station_id)  
        for data in result:
            return data[0]
    
    def _convert_to_station_id(self,station_name):
        result = self.db._get_station_by_name(station_name) 
        for data in result:
            return data[0]

        