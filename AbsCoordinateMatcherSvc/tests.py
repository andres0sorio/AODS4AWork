import unittest
from src.CoordinateMatcher import CoordinateMatcher


class MyTestCase(unittest.TestCase):
    def test_basics(self):

        matcher = CoordinateMatcher('data/equivalence_table.csv')
        input = {1: 105.43, 2: 48.97}
        matcher.match_json_input(input)

    def test_jsonfy(self):

        matcher = CoordinateMatcher('data/equivalence_table.csv')
        input = {1: 105.43, 2: 48.97}
        matcher.match_json_input(input)
        results = matcher.results
        results_dct = {str(i+1): results[i] for i in range(0, len(results))}

        print(results_dct)


if __name__ == '__main__':
    unittest.main()
