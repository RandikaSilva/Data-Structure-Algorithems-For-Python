import psycopg2


def insertStationData(stationID, stationName):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Lasitha@123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PDSA")

        cursor = connection.cursor()

        query = "INSERT INTO station VALUES('" + \
            str(stationID)+"','"+stationName+"');"
        cursor.execute(query)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()


def insertConnectedStationData(stationID, connectedStationID, distance):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Lasitha@123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PDSA")

        cursor = connection.cursor()

        query = "INSERT INTO connected_stations VALUES('"+str(
            stationID)+"','"+str(connectedStationID)+"','"+str(distance)+"');"
        cursor.execute(query)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()


def updateStationData(stationID, stationName):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Lasitha@123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PDSA")

        cursor = connection.cursor()

        query = "UPDATE station SET stationname='"+stationName + \
            "' WHERE stationid = '"+str(stationID)+"';"
        cursor.execute(query)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()


def updateConnectedStationData(stationID, connectedStationID, distance):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Lasitha@123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PDSA")

        cursor = connection.cursor()

        query = "UPDATE connected_stations SET connected_stationid='" + \
            str(connectedStationID)+"', distance='"+str(distance) + \
            "' WHERE stationid='"+str(stationID)+"';"
        cursor.execute(query)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()


def DeleteStationData(stationID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Lasitha@123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="PDSA")

        cursor = connection.cursor()

        query = "DELETE FROM connected_stations WHERE stationid = '" + \
            str(stationID)+"' OR connected_stationid='"+str(stationID)+"';"
        second = "DELETE FROM station WHERE stationid ='"+str(stationID)+"';"
        cursor.execute(query)
        cursor.execute(second)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()


# insertStationData(2, "Lasitha")
insertConnectedStationData(2, 2, 10)
# updateStationData(1, "Lasitha")
# updateConnectedStationData(1,10,10)
