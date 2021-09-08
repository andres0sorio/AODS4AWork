import unittest
from src.GangaConnector import GangaConnector


class MyTestCase(unittest.TestCase):
    def test_script(self):
        gc = GangaConnector()
        arguments = {"date": "2021-09-11", "time": "8:30:00"}
        gc.run(arguments)


if __name__ == '__main__':
    unittest.main()
