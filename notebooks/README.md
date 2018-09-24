Run these files in this order:

1. createTrainingData.ipynb
2. merge_surprise_and_kitso_films.Rmd

But first you will need to download [surprise data ](https://surprise.readthedocs.io/en/stable/dataset.html#dataset) (the movielens-100k dataset). Please move this data to a ml-100k directory in the data directory under this repository root. And you will also need to enter kitso production db credentials in an config.ini file (see config.ini.example) in this directory.