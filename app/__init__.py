import os
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__, instance_relative_config=True)
CORS(app)

from app import api

env = os.environ.get('ENV')
if env == 'prod':
    app.config.from_object('app.config.env_settings.ProductionConfig')
elif env == 'dev':
    conf_filepath = os.path.join(app.root_path, '../config.cfg')
    app.config.from_pyfile(conf_filepath)
