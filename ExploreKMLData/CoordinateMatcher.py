import csv
import logging
import numpy as np
from Extras.Utilities import exportToCSV


class CoordinateMatcher:
    """


    """
    def __init__(self, table_file):
        self.input_file = table_file
        self.table = self.upload_table()
        self.deltas = np.array(self.table["deltas"])
        self.results = []

        try:
            logging.basicConfig(filename='logs/matcher_uploader.log', level=logging.DEBUG)
        except FileNotFoundError:
            print("logging disabled for AccidentDataUploader")

    def upload_table(self):
        """

        :return:
        """
        table = {}
        latitudes = []
        longitudes = []
        elevations = []
        deltas = []

        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=';')
                next(reader)
                for row in reader:
                    latitude = float(row[0])
                    longitude = float(row[1])
                    elevation = float(row[2])
                    delta_x = float(row[3])
                    latitudes.append(latitude)
                    longitudes.append(longitude)
                    elevations.append(elevation)
                    deltas.append(delta_x)

            table["latitudes"] = latitudes
            table["longitudes"] = longitudes
            table["alturas"] = elevations
            table["deltas"] = deltas

            return table

        except IOError as error:
            logging.info(error)

    def match_input(self, input_file):
        """

        :param input_file:
        :return:
        """
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=';')
                next(reader, None)

                for row in reader:
                    pos_x = float(row[2])

                    latitude, longitude, elevation = self.match(pos_x)
                    print(pos_x, latitude, longitude)
                    abs_KM1000 = int(pos_x*1000)
                    self.results.append([abs_KM1000, latitude, longitude, elevation])

        except IOError as error:
            logging.info(error)

    def match(self, x):
        """

        :param x:
        :return:
        """

        idx = (np.abs(self.deltas - x)).argmin()
        latitude = self.table["latitudes"][idx]
        longitude = self.table["longitudes"][idx]
        elevation = self.table["alturas"][idx]

        return latitude, longitude, elevation

    def export(self):
        """

        :return:
        """
        exportToCSV(self.results, 'data/export_coordinates.csv', ["ABS KM*1000", "Latitudes", "Longitudes", "Altura"])

