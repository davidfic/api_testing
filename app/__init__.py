from flask import Flask
from pymongo import MongoClient
from config import *


connection = MongoClient(db_address, int(db_port))

db = connection["api_test"]
collection=db['api_test']
 # MongoLab has user authentication
db.authenticate(db_username, db_password)


app = Flask(__name__)

from app import views
