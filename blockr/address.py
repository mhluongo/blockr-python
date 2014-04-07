"""
This class will handle address related information gathering and managing.
There is not many calls to actual endpoints, so the rest of the methods are more
like helper methods to get data.
"""

from blockr.service import Service

class Address(Service):
    """ The API address class, provies usefull methods for coin addresses.
        Inherits the Service class as a backbone. """

    def info(self, address):
        """ Fetch all info about an address. """
        address = Service.api['address']['info'] + address
        return Service.get(self, address)

    def balance(self, address):
        """ Fetch the address current balance. """
        address = Service.api['address']['balance'] + address
        return Service.get(self, address)

    def transaction(self, address):
        """ Fetch the address transactions. 200 most recent available. """
        address = Service.api['address']['transaction'] + address
        return Service.get(self, address)

    def unspent(self, address):
        """ Fetch the address unspent  """
        address = Service.api['address']['unspent'] + address
        return Service.get(self, address)

    def unconfirmed(self, address):
        """ DOCSTR """
        address = Service.api['address']['unconfirmed'] + address
        return Service.get(self, address)



