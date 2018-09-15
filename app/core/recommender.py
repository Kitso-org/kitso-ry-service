import io
from surprise import KNNBaseline
from surprise import Dataset
from surprise import get_dataset_dir

MOVIES_DATA_PATH = get_dataset_dir() + '/ml-100k/ml-100k/u.item'
MOVIE_ID_INDEX = 0
MOVIE_NAME_INDEX = 1
MOVIE_RELEASE_DATE_INDEX = 2


class Recommender:

    def __init__(self):
        self.train_model()
        self.movie_id_to_name = self._load_movies_info()

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

    def _load_movies_info(self):
        movie_id_to_name = {}
        with io.open(MOVIES_DATA_PATH, 'r', encoding='ISO-8859-1') as f:
            for movie_row in f:
                movie_row = movie_row.split('|')
                movie_id_str = movie_row[MOVIE_NAME_INDEX]
                movie_name_str = movie_row[MOVIE_NAME_INDEX]
                movie_id_to_name[movie_id_str] = movie_name_str
        return movie_id_to_name
