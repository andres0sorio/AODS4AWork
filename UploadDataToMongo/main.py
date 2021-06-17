from accidents.AccidentDataUploader import *


def upload_data():
    accidents = AccidentDataUploader(context, input_file)
    accidents.upload_from_csv()
    accidents.write_to_mongodb(True)


if __name__ == '__main__':

    context = AccidentData()
    context.client = 1001
    context.client_name = "AINSER SAS"
    context.client_contact = "JUAN PEREZ"
    context.client_phone = "57123123123"
    context.data_origin = "VIA Neiva Girardot"

    input_file = 'data/Siniestros autovia.csv'

    upload_data()

    print("All done")