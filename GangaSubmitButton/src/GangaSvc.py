from flask_restful import Resource
from flask import make_response
from flask import render_template
from flask import request
from flask import abort
from flask_cors import cross_origin
from src.GangaConnector import GangaConnector


class GangaSvc(Resource):
    """
    """
    @cross_origin(headers=['Content-Type', 'Authorization'])
    def get(self):
        """
        REST GET Method
        :return: json
        """

        print("OK READY to have some fun with")

        return render_template("form.html")

    @cross_origin(headers=['Content-Type', 'Authorization'])
    def post(self):
        """
        REST POST Method
        :return: json
        """

        try:
            dt = request.form['date']
            tt = request.form['time']
            print("OK READY to have some fun with")
            print(dt, tt)
            arguments = {"date": dt, "time": tt}

            gc = GangaConnector()
            exit_code = gc.run(arguments)
            if exit_code == 1:
                response = {'service_message': 'Job successfully submitted.'}
            else:
                response = {'service_message': 'There was a problem. Please check logs.'}

            return render_template("form.html", **response)

        except Exception as error:
            print(error)
            print("You did something not yet implemented")
            abort(500)
