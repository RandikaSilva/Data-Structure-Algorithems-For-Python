from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/navigate',methods=['POST'])
def navigate():
    print(request.form['name'])
    return "Navigate"

@app.route('/station/update',methods=['POST'])
def update_station(update_data):
    return "Update"  

@app.route('/station/delete',methods=['POST'])
def delete_station(delete_data):
    return "Delete"

@app.route('/station/insert',methods=['POST'])
def insert_station(insert_data):
    return "Insert"

@app.route('/station/view',methods=['GET'])
def view_station(view_data):
    return "View"

if __name__ == '__main__':
   app.run()