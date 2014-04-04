import unittest
from blockr.service import Service

class TestServiceClass(unittest.TestCase):
    """ Tests for the Service class """

    def root_url(self, func, expected):
        """ Testing the root URI generation """
        self.assertEqual(func, expected)

    def setUp(self):
        """ Setting up a few diffrent currencies, and testing base uri. """
        self.ltc = Service('Litecoin')
        self.btc = Service('Bitcoin')
        self.dgc = Service('Digitalcoin')

    def test_bitcoin_base_url_builder(self):
        """ Targetting bitcoin root URI """
        self.root_url(self.btc.base_uri('bitcoin'), 'http://blockr.io/api/v1/')

    def test_litecoin_base_url_builder(self):
        """ Targetting litecoin root URI """
        self.root_url(self.ltc.base_uri('litecoin'), 'http://ltc.blockr.io/api/v1/')

    def test_digitalcoin_base_url_builder(self):
        """ Targetting digitalcoin root URI """
        self.root_url(self.dgc.base_uri('digitalcoin'), 'http://dgc.blockr.io/api/v1/')

    def test_for_not_supported_currency(self):
        """ Should fail with an exeption """

        self.assertRaises(AttributeError, self.btc.lord('common-bennet'))


if __name__ == '__main__':
    unittest.main()
