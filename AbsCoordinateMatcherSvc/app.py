from flask import Flask
from flask_restful import Api
from src.Coordinates import Coordinates

app = Flask(__name__)
api = Api(app)
api.add_resource(Coordinates, '/coordinates')  # '/coordinates' is our entry point
