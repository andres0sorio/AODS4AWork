import unittest
from src.Utilities import *


class MyTestCase(unittest.TestCase):
    def test_encoding(self):
        plate = 'SZS342'
        plate_code = encode_plate(plate)
        print(plate_code)

    def test_decoding(self):
        plate_code = 192619342
        plate = decode_plate(plate_code)
        print(plate)



if __name__ == '__main__':
    unittest.main()
