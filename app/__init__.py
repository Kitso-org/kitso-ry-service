import os
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__, instance_relative_config=True)
CORS(app)

from app import api

conf_filepath = os.path.join(app.root_path, '../config.cfg')
app.config.from_pyfile(conf_filepath)
