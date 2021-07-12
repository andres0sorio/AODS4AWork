from flask import request
from flask_restful import Resource
from .CoordinateMatcher import CoordinateMatcher


class Coordinates(Resource):
    """

    """

    def get(self):
        """
        REST GET Method
        :return: json
        """
        return {'data': 'Ready for your command'}, 200  # return data and 200 OK code

    def post(self):
        """
        REST POST Method receives a json with ABS in KM and returns coordinates
        :return: json
        """
        json_data = request.get_json(force=True)
        matcher = CoordinateMatcher('data/equivalence_table.csv')
        matcher.match_json_input(json_data)
        results = matcher.results
        results_dct = {str(i+1): results[i] for i in range(0, len(results))}

        return {'data': results_dct}, 200  # return data with 200 OK
