import unittest
from Extras.Utilities import *


class MyTestCase(unittest.TestCase):

    def test_distance(self):
        d = distance(2.8873968596085753, 2.8726516219645015, -75.3443901848703, -75.34078516405859)
        google_maps_distance = 1.80  # KM
        delta = 0.07  # 10% +/-
        d_low = google_maps_distance*(1.0-delta)
        d_high = google_maps_distance*(1.0+delta)
        print("*", d)
        self.assertTrue(d_low <= d <= d_high)


if __name__ == '__main__':
    unittest.main()
