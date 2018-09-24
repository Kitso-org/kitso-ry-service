import pandas as pd
import numpy as np
import os
from surprise import NormalPredictor
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise import KNNBaseline
from surprise import Dataset
from surprise import get_dataset_dir

FILE_PATH_RATINGS = os.path.expanduser('../data/training_data.csv')
file_path_movies = os.path.expanduser('../data/movies_data.csv')
file_path_users = os.path.expanduser('../data/ml-100k/u.user')


class Recommender:

    def __init__(self):
        self.__load_rating_data_set()
        self.__load_movies_set()
        self.train_model()
        self.movie_id_to_name = self._load_movies_info()

    def train_model(self):
        self.__load_training_set()

        # Using KNN
        sim_options = {'name': 'pearson_baseline', 'user_based': True}
        self.algo = KNNBaseline(k=25, sim_options=sim_options)

        # Training the model
        self.algo.fit(self.training_set)

    def get_top_n_recommended(self, user_id, n=5):
        return 'return example'

    def _load_movies_info(self):
        movie_id_to_name = {}
        with io.open(MOVIES_DATA_PATH, 'r', encoding='ISO-8859-1') as f:
            for movie_row in f:
                movie_row = movie_row.split('|')
                movie_id_str = movie_row[MOVIE_NAME_INDEX]
                movie_name_str = movie_row[MOVIE_NAME_INDEX]
                movie_id_to_name[movie_id_str] = movie_name_str
        return movie_id_to_name

    def __load_training_set(self):
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(
            self.ratings_set[['user_id', 'item_id', 'rating']], reader)
        self.training_set = data.build_full_trainset()

    def __load_movies_set(self):
        self.movies_set = pd.read_csv(
            file_path_movies, delimiter=';', encoding='latin-1')

    def __load_rating_data_set(self):
        self.ratings_set = pd.read_csv(FILE_PATH_RATINGS, delimiter=';')
