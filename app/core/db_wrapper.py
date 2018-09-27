from pymongo import MongoClient
import configparser

config = configparser.ConfigParser()
config.read('../config/config.ini')

db_user = config['DEFAULT']['DB_USER']
db_name = config['DEFAULT']['DB_NAME']
db_pass = config['DEFAULT']['DB_PASS']

db_url = "mongodb://" + db_user + ":" + db_pass + "@ds237669.mlab.com:37669/" + db_name

client = MongoClient(db_url)
db = client[db_name]

class User(object):    
    def __init__(self, **entries):
        self.__dict__.update(entries)    