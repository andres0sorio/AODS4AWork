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

        km_point_1 = 4.9  # Confamiliar Playa Juncal: 2.8234083232893283, -75.32808114390144
        km_point_2 = 12.5  # Point 2: 2.887096, -75.344258
        km_point_3 = 15.3  # Point 3: Zona Franca: 2.9067294835127058, -75.32901151046433
        km_point_4 = 52.1  # Point 4: Fast Food J&Y 3.2163799682308594, -75.25017608666538
        km_point_5 = 127.0  # Point 5: Parador Maria Jose 3.8193086227629403, -75.06331824461414
        km_point_6 = 171.0 # Punto 6: Monumento a la Tambora: 4.148768410412617, -74.89571437286209

        matcher = CoordinateMatcher('data/equivalence_table.csv')
        latitude, longitude = matcher.match(km_point_1)
        print(latitude, ",", longitude)

        latitude, longitude = matcher.match(km_point_2)
        print(latitude, ",", longitude)

        latitude, longitude = matcher.match(km_point_3)
        print(latitude, ",", longitude)

        latitude, longitude = matcher.match(km_point_4)
        print(latitude, ",", longitude)

        latitude, longitude = matcher.match(km_point_5)
        print(latitude, ",", longitude)

        latitude, longitude = matcher.match(km_point_6)
        print(latitude, ",", longitude)


if __name__ == '__main__':
    unittest.main()
