from surprise import KNNBaseline
from surprise import Dataset

def get_top_n_recommended(user_id, n):

    # Load the movielens-100k dataset (download it if needed).
    data = Dataset.load_builtin('ml-100k')

    # Spliting data in train (85%) and test (15%)
    training_set = data.build_full_trainset()

    # Using KNN
    sim_options={'name': 'pearson_baseline', 'user_based': True}
    algo = KNNBaseline(k=25, sim_options=sim_options)

    # Training the model
    algo.fit(training_set)

    return 'return example'

