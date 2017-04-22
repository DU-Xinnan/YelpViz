import json
from flask import render_template
# from flask import request
# from flask import make_response

from server import app
from server.models.utils import get_class_instance


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data_list')
def get_data_list():
    data_list = ['LasVegas']
    return json.dumps(data_list)


@app.route('/api/data/<dataname>')
def get_data(dataname):
    instance = get_class_instance(dataname)
    return instance.get_data()
