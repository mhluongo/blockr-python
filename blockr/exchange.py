"""
The class will convert current cryptocoin rates
and return the current value in fiat money.
"""

from blockr.service import Service
import simplejson as json

class Exchange(Service):
    """ The class main function is the serve the exchange-rates and do some
    minor tweaks on the data. """

    def exchange(self):
        """ The main caller. Returns a big json dump of data.
            Methods below will do some surgery in the payload. """
        rates = Service.api['exchange']
        return Service.get(self, rates)

    def rate(self, currency):
        """ Returns the current exchange rates """
        current = json.loads(self.exchange())['data'][0]['rates'][currency]
        return round(float(current), 2)

    def fiat(self, currency):
        """ The current value in FIAT currency """
        payload = json.loads(self.exchange())
        fiat_value = float(payload['data'][0]['rates'][currency])
        coin_value = float(payload['data'][0]['rates']['BTC'])
        current = fiat_value * (1 / coin_value)
        return round(current, 2)






