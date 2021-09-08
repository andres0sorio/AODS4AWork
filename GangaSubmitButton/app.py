from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from src.GangaSvc import GangaSvc

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(GangaSvc, '/job')  # '/job data' entry point
