import logging
from src.Utilities import *

na_info = {'province': "NA",  'town': "NA",  'service': "NA"}


class PlateRegistrationPlace:
    """
    Search and assign licence plate registration entity (province, city and destination use Particular-Public)
    Author: Andres Osorio
    Date: 13/07/2021
    Comment: DS4A Project
    """
    def __init__(self):
        self.input_data = "data/MinTrans_vehiculos_placas_2001.csv"
        self.info = []
        try:
            logging.basicConfig(filename='log/plate_registration.log', level=logging.DEBUG)
        except FileNotFoundError:
            print("logging disabled for PlateRegistrationPlace")

        self.records = get_mintransport_data(self.input_data, logging)

        logging.info("Total records:" + str(len(self.records)))

    def prepare_bins(self):
        """

        :return:
        """
        for record in self.records:
            record["range_min"] = encode_plate(record["plate_range_min"])
            record["range_max"] = encode_plate(record["plate_range_max"])

    def match_information(self, input_file):
        """

        :param input_file:
        :return:
        """

        try:
            encoded_plates = []
            with open(input_file, 'r', encoding='utf-8-sig') as f:
                reader = csv.reader(f, delimiter=';')
                for row in reader:
                    plate = row[0]
                    plate_code = encode_plate(plate)
                    # 1. we are for this code version, only looking at CAR PLATES - Ignore MOTORCYCLES
                    if plate_code != 0:
                        encoded_plates.append(plate_code)

            print("All done reading - " + str(len(encoded_plates)))
            encoded_plates.sort()

            for plate_code in encoded_plates:
                plate_info = {}
                search_result = self.search_information(plate_code)
                plate = decode_plate(plate_code)
                plate_info[plate] = search_result
                self.info.append(plate_info)

            print(self.info)
            print("All done search - " + str(len(self.info)))

        except IOError as error:
            logging.info(error)

    def search_information(self, plate):

        for record in self.records:
            if record["range_min"] <= plate <= record["range_max"]:
                return {'province': record["province"],
                        'town': record["town"],
                        'service': record["service"]}

        return na_info

    def export_information(self, output_file):
        """

        :param output_file:
        :return:
        """

        information = []

        for plate_info in self.info:
            plate = list(plate_info.keys())[0]
            info = plate_info[plate]
            information.append([plate, info['province'], info['town'], info['service']])

        exportToCSV(information, output_file, ['PLATE', 'PROVINCE', 'TOWN', 'SERVICE'])


