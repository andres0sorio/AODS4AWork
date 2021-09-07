import requests
import json
import time
from time import sleep
from .Configuration import Configuration
from .Utilities import *


class Experiment:
    """

    """
    def __init__(self):
        """
        """
        config = Configuration()
        self.viz_service = config.get("VIZ_SVC")
        self.api_gateway = config.get("API_SVC")
        self.auth_svc = config.get("AUTH_SVC")

        self.token = ""

    def execute_request(self, mode):

        switcher = {"with_auth": self.send_request_auth, "no_auth": self.send_request}
        func = switcher.get(mode, lambda: 'Invalid')
        return func

    def send_request(self, end_point):
        """

        :return:
        """

        start = time.time()
        url = self.viz_service + end_point
        response = requests.request("GET", url)
        end = time.time()
        print(response.status_code)
        return end - start

    def send_request_auth(self, end_point):
        """

        :return:
        """
        if self.token == "":
            user = {"username": "developer@route90labs.com", "password": "Qwerty123$"}
            response = requests.request("POST", self.auth_svc + "auth", json=user)
            self.token = json.loads(response.text)
            print(response.status_code)
            print(self.token)

        headers = {'Authorization': 'Bearer ' + self.token}

        start = time.time()
        url = self.api_gateway + end_point
        response = requests.get(url, headers=headers)
        end = time.time()
        print(response.status_code)
        return end - start

    def run(self):
        """

        :return:
        """

        with open('data/experiments.json', encoding="utf-8") as f_in:
            experiments = json.load(f_in)

        for experiment in experiments:

            if not experiment["run"]:
                continue

            points = []

            n_times = experiment["ntimes"]
            name = experiment["name"]

            for i in range(0, n_times):

                try:
                    value = self.execute_request(experiment["auth"])(experiment["endpoint"])
                    points.append([str(value)])
                    sleep(0.050)

                except ConnectionError as error:
                    print(error)
                    continue

            output = 'output/experiment_' + name + ".csv"
            exportToCSV(points, output, ['latency'])

