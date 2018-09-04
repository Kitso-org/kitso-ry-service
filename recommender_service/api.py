#!/usr/bin/python
# coding: utf-8
import os
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from core.recommender import get_top_n_recommended

app = Flask(__name__)
CORS(app)

@app.route('/recommendation', methods=['POST'])
def getRecommendation():
    req_data = request.get_json()

    user_id = req_data['user_id']
    n_to_return = req_data['n']

    recommended = get_top_n_recommended(user_id, n_to_return)
    return recommended


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 39007))
    app.debug = True
    app.run(host='127.0.0.1', port=port)
    app.run()