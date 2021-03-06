from accidents.AccidentDataUploader import *


def upload_data():
    accidents = AccidentDataUploader(context, input_file)
    accidents.upload_from_csv()
    accidents.write_to_mongodb(True)


if __name__ == '__main__':

    context = AccidentData()
    context.client = 1001
    context.client_name = "DS4A SAS"
    context.client_contact = "JUAN PEREZ"
    context.client_phone = "57123123123"
    context.data_origin = "VIA X a Z"

    input_file = 'data/all_records.csv'

    upload_data()

    print("All done")