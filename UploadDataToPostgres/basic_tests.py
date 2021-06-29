import unittest
from DataUploader.PgsqlDataUploader import PgsqlDataUploader


class MyTestCase(unittest.TestCase):

    def test_connection(self):

        uploader = PgsqlDataUploader('csvfiles_test.json')
        uploader.drop_table_test()
        uploader.create_table_test()
        uploader.upload_from_csv()
        uploader.clean_up()

    def test_data_size(self):

        uploader = PgsqlDataUploader('csvfiles.json')
        uploader.clean_up()


if __name__ == '__main__':
    unittest.main()
