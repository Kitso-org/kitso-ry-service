from surprise import KNNBaseline
from surprise import Dataset


class Recommender:

    def __init__(self):
        self.train_model()

    def train_model(self):
        # Load the movielens-100k dataset (download it if needed).
        self.data = Dataset.load_builtin('ml-100k')

        # Spliting data in train (85%) and test (15%)
        self.training_set = self.data.build_full_trainset()

        # Using KNN
        sim_options = {'name': 'pearson_baseline', 'user_based': True}
        self.algo = KNNBaseline(k=25, sim_options=sim_options)

        # Training the model
        self.algo.fit(self.training_set)

    def get_top_n_recommended(self, user_id, n=5):
        return 'return example'
