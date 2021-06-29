from DataUploader.PgsqlDataUploader import PgsqlDataUploader


def clean():

    input_file = 'csvfiles.json'
    uploader = PgsqlDataUploader(input_file)
    uploader.run_script("sql/AdventureWorks_postgres_drop.sql")
    uploader.clean_up()


def prepare():

    input_file = 'csvfiles.json'
    uploader = PgsqlDataUploader(input_file)
    uploader.run_script("sql/AdventureWorks_postgres_create_NoRels.sql")
    uploader.clean_up()


def upload():

    input_file = 'csvfiles.json'
    uploader = PgsqlDataUploader(input_file)
    uploader.upload_from_csv()
    uploader.clean_up()


def execute(i):

    switcher = {0: clean, 1: prepare, 2: upload}

    func = switcher.get(i, lambda: 'Invalid')

    return func()


if __name__ == '__main__':
    """
    Little application to make some basic operations on Postgres Databases
    - Clean, Drop, Upload data from scripts
    - Data in CSV format
    - Make use of psycopg2
    
    Author: Andres Osorio
    Date: 27/06/2021
    Company: Phystech SAS
    Client: DS4A Course
    """
    execute(2)

    print("All done")
