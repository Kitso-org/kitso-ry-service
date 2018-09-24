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
FILE_PATH_MOVIES = os.path.expanduser('../data/movies_data.csv')


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

    def get_top_n_recommended(self, user_id, n=5):
        return 'return example'

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
