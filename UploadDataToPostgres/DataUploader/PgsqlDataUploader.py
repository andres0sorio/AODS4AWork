import json
import logging
import psycopg2
from configparser import ConfigParser


class PgsqlDataUploader:
    """clase para tomar datos en formato CSV y subirlos a la BD"""
    def __init__(self, input_file):
        self.input_file = input_file
        self.bulk_data = []

        try:
            logging.basicConfig(filename='logs/pgsql_uploader.log', level=logging.DEBUG)
        except FileNotFoundError:
            print("logging disabled for PgsqlDataUploader")

        # Open the connection to DB
        config = self.config()

        self.conn = None

        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(
                host=config["host"],
                database=config["database"],
                user=config["user"],
                password=config["password"])

            # create a cursor
            cur = self.conn.cursor()

            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def config(filename='config.ini', section='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)
        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db

    def upload_from_csv(self):
        try:
            with open(self.input_file, 'r') as json_input:
                datasets = json.load(json_input)
                for dt in datasets:
                    table = dt["table"]
                    csv_file = dt["file"]

                    cur = self.conn.cursor()

                    try:
                        sql = "COPY \"%s\" FROM STDIN WITH CSV HEADER DELIMITER AS ','"
                        file = open(csv_file, "r", encoding="utf-8")
                        cur.copy_expert(sql=sql % table, file=file)
                        file.close()
                        print("Copy from file " + csv_file + " to " + table + " DONE")
                    except psycopg2.Error as error:
                        print(error)

                    self.conn.commit()

        except IOError as error:
            logging.info(error)

    def clean_up(self):
        if self.conn is not None:
            self.conn.close()
            print('Database connection closed.')

    def drop_table_test(self):
        drop_2 = "DROP TABLE IF EXISTS \"Product\";"
        with self.conn.cursor() as cur:
            cur.execute(drop_2)

    def create_table_test(self):
        file = open("sql/create_test.sql", "r")
        sql_cmd = file.read()
        with self.conn.cursor() as cur:
            cur.execute(sql_cmd)
        file.close()

    def run_script(self, input_file):
        file = open(input_file, "r")
        sql_script = file.read()
        sql_script = sql_script.replace("\n", "")
        commands = sql_script.split(";")
        with self.conn.cursor() as cur:
            for cmd in commands:
                if cmd != "":
                    sql_cmd = cmd + ";"
                    cur.execute(sql_cmd)
        file.close()
        self.conn.commit()
        print("Script executed")
