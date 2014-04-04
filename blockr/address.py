"""
This class will handle address related information gathering and managing.
There is not many calls to actual endpoints, so the rest of the methods are more
like helper methods to get data.
"""

from service import Service

class Address(Service):
    """ The API address class, provies usefull methods for coin addresses.
        Inherits the Service class as a backbone """

    def __init__(self, address, confirmations=0):
        pass

    def info(self, address):
        """ Grab all info about an address """


