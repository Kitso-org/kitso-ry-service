from flask import Flask, request, jsonify
from app.core.recommender import Recommender
from app import app

recommender = Recommender()


@app.route('/recommendation', methods=['POST'])
def getRecommendation():
    req_data = request.get_json()

    user_id = req_data['user_id']
    n_to_return = req_data['n']

    recommended = recommender.get_top_n_recommended(user_id, n_to_return)
    return recommended
