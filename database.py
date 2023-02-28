import pymongo
import config
import certifi

MongoURL = config.MongoClient
ca = certifi.where()
cluster = pymongo.MongoClient(MongoURL, tlsCAFile=ca)
db = cluster[config.db]
player_collection = db[config.players]
captain_collection = db[config.captains]
match_collection = db[config.matches]
team_collection = db[config.teams]
waiting_collection = db[config.waiting]