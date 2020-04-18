# 0 - Dictionary (Hashmap)
# 1 - LinkedList
# 2 - Adjacancy
from flask import Flask, request
import json

from helpers.dictionary_builder import DictionaryBuilder
from helpers.adjacency_builder import AdjacencyMatrixBuilder
from helpers.linkedlist_builder import LinkedListBuilder

class ShortestPath:

    app = Flask(__name__)

    def initialize_services(self):
        self.data_structure_mode = 0

    @app.route('/')
    def _hello_world(self):
        return 'Hello, World!'

    @app.route('/navigate', methods=['POST'])
    def _navigate(self):
        print(request.form['name'])
        return "Navigate"

    @app.route('/station/update', methods=['POST'])
    def _update_station(self,update_data):
        return "Update"

    @app.route('/station/delete', methods=['POST'])
    def _delete_station(self,delete_data):
        return "Delete"

    @app.route('/station/insert', methods=['POST'])
    def _insert_station(self,insert_data):
        return "Insert"

    @app.route('/station/view', methods=['GET'])
    def _view_station(self,view_data):
        return "View"

    def _load_data(self):
        if self.data_structure_mode == 0:
            builder = DictionaryBuilder()
            pass
        elif self.data_structure_mode == 1:
            # Call linkedlist builder method
            pass
        elif self.data_structure_mode == 2:
            # Call adjacancy builder method
            pass

    if __name__ == '__main__':
        app.run()