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

    def get(self, envar):
        """

        :return:
        """
        key_value = os.getenv(envar, 'NONE')
        return key_value
