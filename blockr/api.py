""" The main api class. Ties the classes together """

from blockr.service import Service
from blockr.address import Address
from blockr.exchange import Exchange

class Api(Address, Exchange):
    """ lolpods """

    def __init__(self, currency, data_type="json"):
        Service.__init__(self, currency, data_type)



