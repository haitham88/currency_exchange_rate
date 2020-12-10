import requests
from app.utils.constants_variables import HTTP_200_OK
from app.settings import EXCHANGE_CURRENCY_API_PREFIX


class CurrencyGateway(object):
    def __init__(self, exceptions):
        self.exceptions = exceptions

    def get_exchange_currencies_rate(self, from_currency: str, to_currency: str, date: str):
        try:
            api_url = EXCHANGE_CURRENCY_API_PREFIX + "{}?from={}&to={}".format(date, from_currency, to_currency)
            response = requests.get(url=api_url)
            if response.status_code == HTTP_200_OK:
                return response.json()
            else:
                return None
        except Exception as e:
            exception = self.exceptions.get_exception("getting_data_from_api", e)
            print(exception)