from flask import Flask, request, jsonify, render_template
from algorithms.djikstra import Djikstra
from algorithms.djikstra_ajd_and_sll import Djikstra as DjikstraForOther
from helpers.adjacency_builder import AdjacencyMatrixBuilder
from helpers.linkedlist_builder import LinkedListBuilder
from helpers.dictionary_builder import DictionaryBuilder
from helpers.station_name_mapper import StationMapper
from db.database import Database
from constants.environment import _initialize_environment
from flask_cors import CORS, cross_origin
from algorithms.mst import MST
from constants.errors import ERRORS
import os
import json
import time
import timeit

dictionary_builder = DictionaryBuilder()
adjacency_builder = AdjacencyMatrixBuilder()
linkedlist_builder = LinkedListBuilder()


app = Flask(__name__)

loaded = False

#with app.app_context():
#    if loaded == False:
#        _initialize_environment()
#        os.environ['DATA_MODIFIED'] = "0"
#        os.environ['DATA_STRUCTURE_MODE'] = "1"
#        dictionary_builder._build()
#        adjacency_builder._build()
#        linkedlist_builder._build()
#        loaded = True

CORS(app)

@app.route('/api/navigate', methods=['POST'])
def _navigate():
    DATA_STRUCTURE_MODE = os.environ.get('DATA_STRUCTURE_MODE')
    params = request.get_json()
    start = params['start']
    end = params['end']
    if DATA_STRUCTURE_MODE is '0':
        djikstra = Djikstra(dictionary_builder._get_cache())
        result = djikstra._find_shortest_path(start, end)
        if result['status'] is True:
            response = {
                'status': True,
                'message': 'Request successfull',
                'data':  result['data']
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is '1':
        djikstra = DjikstraForOther(linkedlist_builder._get_cache())
        result = djikstra._find_shortest_path(start, end)
        if result['status'] is True:
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result['data']
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is '2':
        djikstra = DjikstraForOther(adjacency_builder._get_cache())
        result = djikstra._find_shortest_path(start, end)
        if result['status'] is True:
            response = {
                'status': True,
                'message': 'Request successfull',
                'data':  result['data']
            }
            return jsonify(response)
        else:
            return jsonify(result)
    else:
        return ERRORS.get("database")


@app.route('/api/update/station', methods=['POST'])
def _update_station():
    DATA_STRUCTURE_MODE = os.environ.get('DATA_STRUCTURE_MODE')
    params = request.get_json()
    old_station_name = params["old_station_name"]
    station_name = params["station_name"]
    if DATA_STRUCTURE_MODE is "0":
        result = dictionary_builder._update_station(
            old_station_name, station_name)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is "1":
        result = linkedlist_builder._update_station(
            old_station_name, station_name)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is "2":
        result = adjacency_builder._update_station(
            old_station_name, station_name)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    else:
        return ERRORS.get("database")


@app.route('/api/update/station_connection', methods=['POST'])
def _update_station_connector():
    DATA_STRUCTURE_MODE = os.environ.get('DATA_STRUCTURE_MODE')
    params = request.get_json()
    next_station = params["next_station"]
    station = params["station_name"]
    distance = params["distance"]
    if DATA_STRUCTURE_MODE is "0":
        result = dictionary_builder._update_station_connector(
            station, next_station, distance)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is "1":
        result = linkedlist_builder._update_station_connector(
            station, next_station, distance)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is "2":
        result = adjacency_builder._update_station_connector(
            station, next_station, distance)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    else:
        return ERRORS.get("database")


@app.route('/api/delete/station', methods=['POST'])
def _delete_station():
    DATA_STRUCTURE_MODE =os.environ.get('DATA_STRUCTURE_MODE') 
    params = request.get_json()
    station_name = params["station_name"]
    if DATA_STRUCTURE_MODE is "0":
        result = dictionary_builder._delete(station_name)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is "1":
        result = linkedlist_builder._delete(station_name)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is "2":
        result = adjacency_builder._delete(station_name)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    else:
        return ERRORS.get("database")

@app.route('/api/delete/station_connection', methods=['POST'])
def _delete_station_connection():
    DATA_STRUCTURE_MODE =os.environ.get('DATA_STRUCTURE_MODE') 
    params = request.get_json()
    station_name = params["station_name"]
    next_station = params["next_station"]
    if DATA_STRUCTURE_MODE is "0":
        result = dictionary_builder._delete_connection(
            station_name, next_station)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is "1":
        result = linkedlist_builder._delete_connection(
            station_name, next_station)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is "2":
        result = adjacency_builder._delete_connection(
            station_name, next_station)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    else:
        return ERRORS.get("database")


@app.route('/api/add/station', methods=['POST'])
def _insert_station():
    DATA_STRUCTURE_MODE =os.environ.get('DATA_STRUCTURE_MODE') 
    params = request.get_json()
    station_name = params["station_name"]
    if DATA_STRUCTURE_MODE is '0':
        result = dictionary_builder._add_station(station_name)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is '1':
        result = linkedlist_builder._add_station(station_name)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is '2':
        result = adjacency_builder._add_station(station_name)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    else:
        return ERRORS.get("database")


@app.route('/api/add/station_connector', methods=['POST'])
def _insert_station_connector():
    DATA_STRUCTURE_MODE =os.environ.get('DATA_STRUCTURE_MODE') 
    params = request.get_json()
    station_name = params["station_name"]
    next_station = params["next_station"]
    distance = params["distance"]
    if DATA_STRUCTURE_MODE is '0':
        result = dictionary_builder._add_station_connector(
            station_name, next_station, distance)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is '1':
        result = linkedlist_builder._add_station_connector(
            station_name, next_station, int(distance))
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is '2':
        result = adjacency_builder._add_station_connector(
            station_name, next_station, distance)
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            return jsonify(result)
    else:
        return ERRORS.get("database")


@app.route('/api/get/all_stations', methods=['GET'])
def _view_station():
    DATA_STRUCTURE_MODE =os.environ.get('DATA_STRUCTURE_MODE')
    if DATA_STRUCTURE_MODE is '0':
        result = dictionary_builder._get_all()
        if result is not None:
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            response = {
                'status': False,
                'message': 'No data'
            }
            return jsonify(response)
    elif DATA_STRUCTURE_MODE is '1':
        result = linkedlist_builder._get_all()
        if result is not None:
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            response = {
                'status': False,
                'message': 'No data'
            }
            return jsonify(response)
    elif DATA_STRUCTURE_MODE is '2':
        result = adjacency_builder._get_all()
        if result is not None:
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result
            }
            return jsonify(response)
        else:
            response = {
                'status': False,
                'message': 'No data'
            }
            return jsonify(response)
    else:
        return ERRORS.get("database")


@app.route('/api/get/all_stations_connections', methods=['GET'])
def _view_station_connections():
    DATA_STRUCTURE_MODE =os.environ.get('DATA_STRUCTURE_MODE') 
    if DATA_STRUCTURE_MODE is '0':
        result = dictionary_builder._get_all_connections()
        if result["status"] is True:
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result["data"]
            }
            return jsonify(response)
        else:
            response = {
                'status': False,
                'message': 'No data'
            }
            return jsonify(response)
    elif DATA_STRUCTURE_MODE is '1':
        result = linkedlist_builder._get_all_connections()
        if result['status'] is True:
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result['data']
            }
            return jsonify(response)
        else:
            return jsonify(result)
    elif DATA_STRUCTURE_MODE is '2':
        result = adjacency_builder._get_all_connections()
        if result['status'] is True:
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': result['data']
            }
            return jsonify(response)
        else:
            return jsonify(result)
    else:
        return ERRORS.get("database")


@app.route('/api/reset_cache', methods=['GET'])
def _reset_cache():
    DATA_STRUCTURE_MODE =os.environ.get('DATA_STRUCTURE_MODE')
    if DATA_STRUCTURE_MODE is '0':
        result = dictionary_builder._reset_cache_dictionary()
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': None
            }
            return jsonify(response)
        else:
            response = {
                'status': False,
                'message': "Unable to reset"
            }
            return jsonify(response)
    elif DATA_STRUCTURE_MODE is '1':
        result = linkedlist_builder._reset_cache_linkedlist()
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': None
            }
            return jsonify(response)
        else:
            response = {
                'status': False,
                'message': "Unable to reset"
            }
            return jsonify(response)
    elif DATA_STRUCTURE_MODE is '2':
        result = adjacency_builder._reset_cache_adjacency()
        if result is True:
            os.environ["DATA_MODIFIED"] = "1"
            response = {
                'status': True,
                'message': 'Request successfull',
                'data': None
            }
            return jsonify(response)
        else:
            response = {
                'status': False,
                'message': "Unable to reset"
            }
            return jsonify(response)
    else:
        return ERRORS.get("database")


@app.route('/api/mode/change', methods=['POST'])
def _change_data_structure():
    params = request.get_json()
    mode = params['mode']
    result = setMode(mode)
    if result['status'] is True:
        response = {
            'status': True,
            'message': 'Mode changed',
            'data': None
        }
        return jsonify(response)
    else:
        response = {
            'status': False,
            'message': "Unable to change"
        }
        return jsonify(response)


@app.route('/api/mode/get', methods=['GET'])
def _get_data_structure():
    DATA_STRUCTURE_MODE =os.environ.get('DATA_STRUCTURE_MODE') 
    response = {
        'status': True,
        'message': 'Request successfull',
        'data': DATA_STRUCTURE_MODE
    }
    return jsonify(response)


@app.route('/api/load_data')
def _load_data():
    DATA_MODIFIED = os.environ.get("DATA_MODIFIED")
    if DATA_MODIFIED == "1":
        DATA_STRUCTURE_MODE =os.environ.get('DATA_STRUCTURE_MODE') 
        if DATA_STRUCTURE_MODE is '0':
            dictionary_builder._build()
        elif DATA_STRUCTURE_MODE is '1':
            linkedlist_builder._build()
        elif DATA_STRUCTURE_MODE is '2':
            adjacency_builder._build()
        response = {
            'status': True,
            'message': 'Request successfull',
            'data': None
        }
        return jsonify(response)
    else:
        response = {
            'status': False,
            'message': 'You already have update data cache',
            'data': None
        }
        return jsonify(response)

@app.route('/api/find_minimum_path',methods=['POST'])
def _find_minimum_path():
    params = request.get_json()
    selected_stations = params["selected_stations"]
    DATA_STRUCTURE_MODE = os.environ.get('DATA_STRUCTURE_MODE')
    if DATA_STRUCTURE_MODE is '0':
        mst = MST()
        result=mst._get_mst(selected_stations,dictionary_builder)
        return result
    elif DATA_STRUCTURE_MODE is '1':
        mst = MST()
        result=mst._get_mst(selected_stations,linkedlist_builder)
        return result
    elif DATA_STRUCTURE_MODE is '2':
        mst = MST()
        result= mst._get_mst(selected_stations,adjacency_builder)
        return result

@app.route('/')
def _root():
    return render_template('index.html')

@app.errorhandler(404)
def _page_not_found(e):
    return render_template('index.html')


def setMode(mode):
    db = Database()
    result = db._set_mode(mode)
    return result


def getMode():
    db = Database()
    result = db._get_mode()
    if result['status'] is True:
        return result['data']


if __name__ == "__main__":
    _initialize_environment()
    os.environ['DATA_MODIFIED'] = "0"
    os.environ['DATA_STRUCTURE_MODE'] = "1"

    start_time = time.time()
    dictionary_builder._build()
    print(str(time.time() - start_time)+" Dictionary build")

    start_time = time.time()
    adjacency_builder._build()
    print(str(time.time() - start_time)+" LinkedList build")

    start_time = time.time()
    linkedlist_builder._build()
    print(str(time.time() - start_time)+" Adjacency build")

    app.run()
