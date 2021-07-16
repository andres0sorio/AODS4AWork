import unittest
from Extras.Utilities import *
from CoordinateMatcher import CoordinateMatcher


class MyTestCase(unittest.TestCase):

    def test_distance(self):
        d = distance(2.8873968596085753, 2.8726516219645015, -75.3443901848703, -75.34078516405859)
        google_maps_distance = 1.80  # KM
        delta = 0.07  # 10% +/-
        d_low = google_maps_distance*(1.0-delta)
        d_high = google_maps_distance*(1.0+delta)
        print("*", d)
        self.assertTrue(d_low <= d <= d_high)

    def test_matcher(self):
        """
        KM0+000 = 2.790815780279914, -75.30855836484821
        :return:
        """

        validation_points = [{"point": "km_point_1",
                               "km": 4.9,
                               "latitude": 2.8234083232893283,
                               "longitude": -75.32808114390144},
                             {"point": "km_point_2",
                               "km": 12.5,
                               "latitude": 2.887096,
                               "longitude": -75.344258},
                             {"point": "km_point_3",
                               "km": 15.3,
                               "latitude": 2.9067294835127058,
                               "longitude": -75.32901151046433},
                             {"point": "km_point_4",
                               "km": 52.1,
                               "latitude": 3.2163799682308594,
                               "longitude": -75.25017608666538},
                             {"point": "km_point_5",
                               "km": 127.0,
                               "latitude": 3.8193086227629403,
                               "longitude": -75.06331824461414},
                             {"point": "km_point_6",
                              "km": 151.0,
                              "latitude": 4.010429856247179,
                              "longitude": -74.97652818616747},
                             {"point": "km_point_7",
                              "km": 158.0,
                              "latitude": 4.0483533198430655,
                              "longitude": -74.95720260352158}
                             ]

        matcher = CoordinateMatcher('data/equivalence_table.csv')

        for point in validation_points:

            latitude, longitude = matcher.match(point["km"])
            aprox_error = distance(latitude, point["latitude"], longitude, point["longitude"])
            print(point["km"], latitude, ",", longitude, aprox_error)


if __name__ == '__main__':
    unittest.main()
