import csv
import json
import datetime
import logging
from pymongo import MongoClient

from .FullAccidentData import *
from .PostAccidentEvents import *


class AccidentDataUploader:
    """clase para tomar datos en formato CSV y subirlos a la BD"""
    def __init__(self, context, input_file):
        self.context = context
        self.input_file = input_file
        self.bulk_data = []

        with open('accidents/config/config.json', 'r') as f:
            config = json.load(f)
            dburl = config['DEV']['DBURL']
            dbport = int(config['DEV']['DBPORT'])
            self.client = MongoClient(dburl, dbport)
            self.db = self.client.ds4a
            self.collection = self.db.project

        try:
            logging.basicConfig(filename='logs/accident_uploader.log', level=logging.DEBUG)
        except FileNotFoundError:
            print("logging disabled for AccidentDataUploader")

    def upload_from_csv(self):
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=';')
                for row in reader:
                    try:
                        data = FullAccidentData(self.context)
                        data.set_id_accident(row[0])
                        data.set_date(row[1])
                        data.set_day_week(row[2])
                        data.set_month(row[3])
                        data.set_year(row[4])
                        data.set_location(row[5])
                        data.set_abs_design(row[6])
                        data.set_n_incident(row[7])
                        data.set_vehicles_involved(row[8])
                        data.set_total_injured(row[9])
                        data.set_total_death(row[10])
                        data.set_total_minor_injured(row[11])
                        data.set_total_serious_injured(row[12])
                        data.set_accident_class(row[13])
                        data.set_infrastructure_affected(row[14])
                        data.set_accident_type(row[15])
                        data.set_accident_cause(row[16])
                        data.set_conditions(row[17])
                        data.set_description(row[27])

                        post_events = PostAccidentEvents()
                        post_events.first_call_time = row[18]
                        post_events.set_arrival_time(row[19])
                        post_events.set_response_time(row[20])
                        post_events.set_ambulance_dep_time(row[21])
                        post_events.set_ambulance_arr_time(row[22])
                        post_events.set_hospital(row[23])
                        post_events.set_ambulance_required(row[24])
                        post_events.set_time_departure_from_base(row[25])
                        post_events.set_time_arrival_to_base(row[26])

                        data.post_accident_actions = post_events.__dict__

                        print(data.id_accident)

                        accident_json = data.__dict__

                        self.bulk_data.append(accident_json)

                    except ValueError:
                        print('There is a wrong data format entry. Please check')
                        logging.info('There is a wrong data format entry. Please check')
                        continue

        except IOError as error:
            logging.info(error)

    def write_to_mongodb(self, is_test):
        if is_test:
            self.collection.drop()
        obj_id = self.collection.insert_many(self.bulk_data)
        print(obj_id)
