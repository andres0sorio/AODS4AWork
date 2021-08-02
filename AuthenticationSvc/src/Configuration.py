import os


class Configuration(object):
    """
    Configuration singleton
    Author: Andres Osorio
    Date: 01/08/2021
    """
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Configuration, cls).__new__(cls)
        return cls.instance

    def getSecretKey(self):
        """

        :return:
        """
        return os.getenv('SECRET_KEY', 'NOSECRET')

    def getUserTable(self):
        """

        :return:
        """
        test_mode = os.getenv('DEBUG', 'YES')
        if test_mode is "YES":
            return "user_tests"
        else:
            return "users"
