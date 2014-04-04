"""
This class contains the fundamental parts of the API wrapper. The class job
is to bootstrap the API with defaults to work with the Blockr.io API
"""
import requests as r

class Service(object):
    """ The API service class, provies the backbone for the Api. Mostly
        bootstrapping, and setup stuff. """

    api = {
        'base': '',
        'version': 'api/v1/',
        'uri': 'blockr.io/',
        'exchange': 'exchangerate/current/',
        'coin': {
            'info': 'coin/info/',
        },
        'block': {
            'info': 'block/info/',
            'transaction': 'block/txs/',
            'raw': 'block/raw/',
        },
        'transaction': {
            'info': 'tx/info/',
            'unconfirmed': 'zerotx/info/',
            'raw': 'tx/raw/',
        },
        'address': {
            'info': 'address/info/',
            'balance': 'address/balance/',
            'transaction': 'address/txs/',
            'unspent': 'address/unspent/',
            'unconfirmed': 'address/unconfirmed/',
        },
        'currencies': {
            'available': [
                'litecoin',
                'bitcoin',
                'digitalcoin',
                'quarkcoin',
                'peercoin',
                'megacoin'
            ]
        }
    }

    def __init__(self, currency, data_type="json"):
        """ Set the user currency, and check if its allowed. Else throw
            and exeption. """
        self.data_type = data_type
        self.currency = currency = currency.lower()

    def base_uri(self, currency):
        """ Build the base URI for the current session. """
        if currency == 'bitcoin':
            self.api['base'] = ''

        if currency == 'litecoin':
            self.api['base'] = 'ltc.'

        if currency == 'digitalcoin':
            self.api['base'] = 'dgc.'

        if currency == 'quarkcoin':
            self.api['base'] = 'qrk.'

        if currency == 'peercoin':
            self.api['base'] = 'ppc.'

        if currency == 'megacoin':
            self.api['base'] = 'mec.'

        if currency not in self.api['currencies']['available']:
            raise Exception(
                """
                Only {1} are supported. The currency: "{0}" is not supported.
                """.format(currency, self.api['currencies']['available']))

        return 'http://{0}{1}{2}'.format(
            self.api['base'], self.api['uri'], self.api['version']
            )

    def get(self, request_uri):
        """ The function that calls the API. All calls go thru this method """
        r.get(self.base_uri(self.currency))
        if self.data_type == 'json':
            return request_uri.json()
        if self.data_type == 'text':
            return request_uri.text
