import os
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

from flask import request, jsonify
from core.recommender import Recommender

recommender = Recommender()


@app.route('/recommendation', methods=['POST'])
def getRecommendation():
    req_data = request.get_json()

    user_id = req_data['user_id']
    n_to_return = req_data['n']

    recommended = recommender.get_top_n_recommended_movies(
        user_id, n_to_return)
    return recommended


@app.route('/test', methods=['GET'])
def getTest():
    return "Live"
