from flask import Flask, request, jsonify
from algorithms.djikstra import Djikstra
from algorithms.djikstra_ajd_and_sll import Djikstra as DjikstraForOther
from data.adjacency import ADJACENCY
from data.dictionary import DICTIONARY
from data.linked_list import LINKEDLIST
from helpers.adjacency_builder import AdjacencyMatrixBuilder
from helpers.linkedlist_builder import LinkedListBuilder
from helpers.dictionary_builder import DictionaryBuilder
from helpers.station_name_mapper import StationMapper
import os
import json

app = Flask(__name__)
station_mapper = StationMapper()

@app.route('/')
def _hello_world():
    return 'Hello, World!'

@app.route('/navigate', methods=['POST'])
def _navigate():
    DATA_STRUCTURE_MODE = os.environ.get('DATA_STRUCTURE_MODE')
    params = request.form
    # station_mapper._convert_to_station_id(params['start'])
    start = params['start']
    end = params['end']  # station_mapper._convert_to_station_id(params['end'])
    if DATA_STRUCTURE_MODE is '0':
        print('Using DICTIONARY')
        djikstra = Djikstra(DICTIONARY)
        result = djikstra._find_shortest_path(start, end)
        return jsonify(result)
    elif DATA_STRUCTURE_MODE is '1':
        print('Using LINKEDLIST')
        djikstra = DjikstraForOther(LINKEDLIST)
        result = djikstra._find_shortest_path(start, end)
        return jsonify(result)
    elif DATA_STRUCTURE_MODE is '2':
        print('Using ADJACENCY')
        djikstra = DjikstraForOther(ADJACENCY)
        result = djikstra._find_shortest_path(start, end)
        return jsonify(result)

@app.route('/update/station', methods=['POST'])
def _update_station():
    DATA_STRUCTURE_MODE = os.environ.get('DATA_STRUCTURE_MODE')
    params = request.form
    old_station_name = params['old_station_name']
    station_name = params['station_name']
    if DATA_STRUCTURE_MODE is "0":
        builder = DictionaryBuilder()
        builder._update_station(old_station_name, station_name)
        print(DICTIONARY)
        return "Done"
    elif DATA_STRUCTURE_MODE is "1":
        builder = LinkedListBuilder()
        builder._update_station(old_station_name, station_name)
        LINKEDLIST._print_graph()
        return "Done"
    elif DATA_STRUCTURE_MODE is "2":
        builder = AdjacencyMatrixBuilder()
        builder._update_station(old_station_name, station_name)
        print(ADJACENCY.adjacency_matrix)
        return "Done"

@app.route('/update/station_connector', methods=['POST'])
def _update_station_connector():
    DATA_STRUCTURE_MODE = os.environ.get('DATA_STRUCTURE_MODE')
    params = request.form
    next_station = params['next_station']
    station = params['station_name']
    distance = params['distance']
    if DATA_STRUCTURE_MODE is "0":
        builder = DictionaryBuilder()
        builder._update_station_connector(station, next_station, distance)
        return DICTIONARY
    elif DATA_STRUCTURE_MODE is "1":
        builder = LinkedListBuilder()
        builder._update_station_connector(station, next_station, distance)
        LINKEDLIST._print_graph()
        return "Done"
    elif DATA_STRUCTURE_MODE is "2":
        builder = AdjacencyMatrixBuilder()
        builder._update_station_connector(station, next_station, distance)
        print(ADJACENCY.adjacency_matrix)
        return "Done"

@app.route('/station/delete', methods=['POST'])
def _delete_station():
    DATA_STRUCTURE_MODE = os.environ.get('DATA_STRUCTURE_MODE')
    params = request.form
    station_name = params['station_name']
    if DATA_STRUCTURE_MODE is "0":
        builder = DictionaryBuilder()
        builder._delete(station_name)
        return DICTIONARY
    elif DATA_STRUCTURE_MODE is "1":
        builder = LinkedListBuilder()
        builder._delete(station_name)
        return "Done"
    elif DATA_STRUCTURE_MODE is "2":
        builder = AdjacencyMatrixBuilder()
        builder._delete(station_name)
        print(ADJACENCY.adjacency_matrix)
        return "Done"
    return "Done"

@app.route('/add/station', methods=['POST'])
def _insert_station():
    params = request.form
    DATA_STRUCTURE_MODE = os.environ.get('DATA_STRUCTURE_MODE')
    if DATA_STRUCTURE_MODE is '0':
        builder = DictionaryBuilder()
        builder._add_station(params['station_name'])
        print(DICTIONARY)
        return "Added"
    elif DATA_STRUCTURE_MODE is '1':
        builder = LinkedListBuilder()
        builder._add_station(params['station_name'])
        print(LINKEDLIST._print_graph())
        return "Added"
    elif DATA_STRUCTURE_MODE is '2':
        builder = AdjacencyMatrixBuilder()
        builder._add_station(params['station_name'])
        print(ADJACENCY.adjacency_matrix)
        return "Added"
    return "Failed"

@app.route('/add/station_connector', methods=['POST'])
def _insert_station_connector():
    params = request.form
    DATA_STRUCTURE_MODE = os.environ.get('DATA_STRUCTURE_MODE')
    if DATA_STRUCTURE_MODE is '0':
        builder = DictionaryBuilder()
        builder._add_station_connector(
            params['station_name'], params['next_station'], params['distance'])
        print(DICTIONARY)
        return "Done"
    elif DATA_STRUCTURE_MODE is '1':
        builder = LinkedListBuilder()
        builder._add_station_connector(
            params['station_name'], params['next_station'], int(params['distance']))
        print(LINKEDLIST._print_graph())
        return "Done"
    elif DATA_STRUCTURE_MODE is '2':
        builder = AdjacencyMatrixBuilder()
        builder._add_station_connector(
            params['station_name'], params['next_station'], params['distance'])
        print(ADJACENCY.adjacency_matrix)
        return "Done"

@app.route('/view/station', methods=['GET'])
def _view_station():
    return "View"

@app.route('/change/mode', methods=['GET'])
def _change_data_structure():
    mode = request.form['mode']
    os.environ.update({'DATA_STRUCTURE_MODE': mode})

    return "Data structure changed"

def start():
    app.run()
