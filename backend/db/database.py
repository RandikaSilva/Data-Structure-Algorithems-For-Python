import psycopg2
import os

class Database:
    def connect(self):
        env = os.environ
        self.connection = psycopg2.connect(user=env.get('DATABASE_USER'), password=env.get('DATABASE_PASSWORD'), host=env.get(
            'DATABASE_HOST'), port=env.get('DATABASE_PORT'), database=env.get('DATABASE_NAME'))

    def _insert_station_data(self, station_id, station_name):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "INSERT INTO station VALUES('" + \
                str(station_id)+"','"+station_name+"');"
            self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error with database,", error)
        finally:
            if self.connection.closed==0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _insert_connected_station_data(self, station_id, connected_station_id, distance):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "INSERT INTO connected_station VALUES('"+str(
                station_id)+"','"+str(connected_station_id)+"','"+str(distance)+"')"
            self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error with database,", error)
        finally:
            if self.connection.closed==0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _update_station_data(self, station_id, station_name):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "UPDATE station SET station_name='"+station_name + \
                "' WHERE station_id = '"+str(station_id)+"''"
            self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error with database,", error)
        finally:
            if self.connection.closed==0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _update_connected_station_data(self, station_id, connected_station_id, distance):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "UPDATE connected_station SET next_station='" + \
                str(connected_station_id)+"',distance='"+str(distance) + \
                "' WHERE station_id='"+str(station_id)+"''"
            self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error with database,", error)
        finally:
            if self.connection.closed==0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _delete_station_data(self, station_id):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "DELETE FROM connected_station WHERE station_id = '" + str(station_id)+"'"
            second = "DELETE FROM station WHERE stationid ='" + \
                str(station_id)
            self.cursor.execute(query)
            self.cursor.execute(second)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error with database,", error)
        finally:
            if self.connection.closed==0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()
    
    def _get_all_connected_stations(self):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM connected_station"
            self.cursor.execute(query)
            result = self.connection.commit()
            return result
        except (Exception, psycopg2.Error) as error:
            print("Error with database,", error)
        finally:
            if self.connection.closed==0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()
