from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='../client/static',
        template_folder="../client")
app.config.from_object('config')
CORS(app)

from server.routes import index
