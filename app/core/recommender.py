import pandas as pd
import numpy as np
import os
from operator import itemgetter
from surprise import NormalPredictor
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise import KNNBaseline
from surprise import Dataset
from surprise import get_dataset_dir
from flask import jsonify

import os
working_dir = os.getcwd()
print("uen --------------------------------")

FILE_PATH_RATINGS = working_dir + "/../data/training_data.csv"
FILE_PATH_MOVIES = working_dir + "/../data/movies_data.csv"


class Recommender:

    def __init__(self):
        self.__load_rating_data_set()
        self.__load_movies_set()
        self.train_model()

    def train_model(self):
        self.__load_training_set()

        # Using KNN
        sim_options = {'name': 'pearson_baseline', 'user_based': True}
        self.algo = KNNBaseline(k=25, sim_options=sim_options)

        # Training the model
        self.algo.fit(self.training_set)

    def __get_not_rated_movies(self, user_id):
        m_ratings = \
            self.ratings_set.loc[
                self.ratings_set.user_id == user_id]

        rated_movies = list(m_ratings.item_id)

        not_rated = \
            [mid
                if (mid not in rated_movies)
                else None
             for mid in self.ratings_set.item_id.unique()]

        return list(not_rated)

    def __filter_by_movies_saved_in_kitso(self, preditions):
        kitso_movies_ids = list(self.movies_set.id)
        movies_id = list(map(lambda tupl: tupl[0], preditions))
        return list(filter(lambda movie_id: movie_id in kitso_movies_ids, movies_id))

    def __search_in_list_of_tuples(self, elem, list_tuples):
        tuples_with_elem = list(filter(lambda tup: elem in tup, list_tuples))
        return elem if len(tuples_with_elem) > 0 else False

    def __predict_rating(self, user_id, movies_ids):
        predicted_rating = []

        for mid in movies_ids:
            predition = self.algo.predict(user_id, mid)
            predition_tuple = (mid, float(predition.est))

            if not self.__search_in_list_of_tuples(mid, predicted_rating):
                predicted_rating.append(predition_tuple)

        return predicted_rating

    def get_top_n_recommended_movies(self, user_id, n=5):

        not_rated = self.__get_not_rated_movies(user_id)

        rating_preditions = self.__predict_rating(user_id, not_rated)

        rating_preditions = self.__filter_by_movies_saved_in_kitso(
            rating_preditions)

        sorted_preditions = sorted(
            rating_preditions, key=itemgetter(1), reverse=True)[:n]

        response = self.movies_set[self.movies_set.id.isin(sorted_preditions)]

        return jsonify(response.to_dict('records'))

    def __load_training_set(self):
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(
            self.ratings_set[['user_id', 'item_id', 'rating']], reader)
        self.training_set = data.build_full_trainset()

    def __load_movies_set(self):
        self.movies_set = pd.read_csv(
            FILE_PATH_MOVIES, delimiter=';', encoding='latin-1')

    def __load_rating_data_set(self):
        self.ratings_set = pd.read_csv(FILE_PATH_RATINGS, delimiter=';')
