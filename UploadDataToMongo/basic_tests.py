import unittest

from accidents.AccidentDataUploader import *


class TestDataObjectsConsistency(unittest.TestCase):

    context = AccidentData()
    context.client = 1001
    context.client_name = "AINSER SAS"
    context.client_contact = "JUAN PEREZ"
    context.client_phone = "57123123123"
    context.data_origin = "VIA Neiva Girardot"

    input_file = 'test_data/first_10_records.txt.csv'

    def test_readingCSV(self):

        accidents = AccidentDataUploader(self.context, self.input_file)
        accidents.upload_from_csv()

    def test_writeToDB(self):

        accidents = AccidentDataUploader(self.context, self.input_file)
        accidents.upload_from_csv()
        accidents.write_to_mongodb(True)


if __name__ == '__main__':
    unittest.main()
