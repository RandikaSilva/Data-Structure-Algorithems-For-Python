from constants.errors import ERRORS
import psycopg2
import os

class Database:
    def connect(self):
        env = os.environ
        self.connection=None
        self.connection = psycopg2.connect(user=env.get('DATABASE_USER'), password=env.get('DATABASE_PASSWORD'), host=env.get(
            'DATABASE_HOST'), port=env.get('DATABASE_PORT'), database=env.get('DATABASE_NAME'))

    def _insert_station_data(self, station_name):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "INSERT INTO station(station_name) VALUES('" + \
                station_name+"')"
            self.cursor.execute(query)
            self.connection.commit()
            return {
                'status':True,
                'data':None
            }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _insert_connected_station_data(self, station, connected_station, distance):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "INSERT INTO connected_station VALUES('"+station + \
                "','"+connected_station+"','"+distance+"')"
            self.cursor.execute(query)
            self.connection.commit()
            return {
                'status':True,
                'data':None
            }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _update_station_data(self, station, station_name):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "UPDATE station SET station_name='"+station_name + "' WHERE station_name = '"+str(station)+"'"
            query_two="UPDATE connected_station SET station='"+station_name + "' WHERE station = '"+str(station)+"'"
            query_three="UPDATE connected_station SET next_station='"+station_name + "' WHERE next_station = '"+str(station)+"'"
            self.cursor.execute(query)
            self.cursor.execute(query_two)
            self.cursor.execute(query_three)
            self.connection.commit()
            return {
                'status':True,
                'data':None
            }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _update_connected_station_data(self, station, connected_station, distance):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "UPDATE connected_station SET distance='"+distance+"' WHERE station='"+str(station)+"' AND next_station='"+str(connected_station)+"' "
            self.cursor.execute(query)
            self.connection.commit()
            return {
                'status':True,
                'data':None
            }
        except (psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _delete_station_data(self, station):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "DELETE FROM connected_station WHERE station = '" + \
                str(station)+"' OR next_station = '"+str(station)+"'"
            second = "DELETE FROM station WHERE station_name ='" + str(station)+"'"
            self.cursor.execute(query)
            self.cursor.execute(second)
            self.connection.commit()
            return {
                'status':True,
                'data':None
            }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _delete_station_connection(self, station,next_station):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "DELETE FROM connected_station WHERE station = '" + \
                str(station)+"' AND next_station = '"+str(next_station)+"'"
            self.cursor.execute(query)
            self.connection.commit()
            return {
                'status':True,
                'data':None
            }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _get_all_connected_stations(self):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM connected_station"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return {
                'status':True,
                'data':result
            }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _get_all_stations(self):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM station"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return {
                'status':True,
                'data':result
            }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _get_station_count(self):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "SELECT COUNT(station_id) FROM station"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return {
                'status':True,
                'data':result
            }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _get_station_by_name(self, station_name):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "SELECT station_id FROM station WHERE station_name='"+station_name+"'"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return {
                'status':True,
                'data':result
            }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _get_station_by_id(self, station_id):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "SELECT station_name FROM station WHERE station_id='"+station_id+"'"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return {
                'status':True,
                'data':result
            }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _get_mode(self):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "SELECT mode FROM data_mode"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for data in result:
                return {
                    'status':True,
                    'data':data[0]
                }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()

    def _set_mode(self,mode):
        try:
            self.connect()
            self.cursor = self.connection.cursor()
            query = "UPDATE data_mode SET mode='"+mode+"' WHERE id=1"
            self.cursor.execute(query)
            self.connection.commit()
            return {
                'status':True,
                'data':[]
            }
        except (Exception, psycopg2.Error):
            return ERRORS.get("database")
        finally:
            if self.connection==None:
                return ERRORS.get("database")
            if self.connection.closed == 0:
                self.connection.close()
            elif not self.cursor.closed:
                self.cursor.close()
