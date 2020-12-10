from app.gateway.exchnage_gateway import CurrencyGateway
from app.databases.mysql_db import Mysql
from app.parsers.currency_parser import currency_rate_repository_parser, currency_rate_gateway_parser
from app.repositories.currency_repository import CurrencyRepository
from app.utils.response import Response
from app.utils.constants_variables import HTTP_200_OK, HTTP_400_BAD_REQUEST
from app.utils.exceptions import Exceptions

class CurrencyAPI(object):
    def __init__(self):
        self.mysql = Mysql()
        self.exceptions = Exceptions()
        self.currency_gateway = CurrencyGateway(self.exceptions)
        self.currency_repository = CurrencyRepository(self.mysql.sessionLocal(), self.exceptions)

    def exchange_currency(self, from_currency, to_currency, date):
        response = Response()
        currency_rate = {}

        try:
            result = self.currency_repository.get(from_currency=from_currency, to_currency=to_currency, date=date)
            if result:
                print("////////////////////////////////////////////////////////////")
                print("GET FROM DATABASE")
                print("////////////////////////////////////////////////////////////")
                currency_rate = currency_rate_repository_parser(result)
            else:
                result = self.currency_gateway.get_exchange_currencies_rate(from_currency, to_currency, date)
                if result:
                    print("////////////////////////////////////////////////////////////")
                    print("GET FROM API")
                    print("////////////////////////////////////////////////////////////")
                    currency_rate = currency_rate_gateway_parser(result)
                    self.currency_repository.create(**currency_rate)

                else:
                    response.status = False
                    response.status_code = HTTP_400_BAD_REQUEST
                    response.data = {"message": "make sure the from_currency code or the to_currency code are right"}
                    return response

            response.status = True
            response.status_code = HTTP_200_OK
            response.data = currency_rate

        except Exception as e:
            print(e)
            response.status = False
            response.status_code = HTTP_400_BAD_REQUEST
            response.data = {"message": self.exceptions.get_exception(None, e.args[0])}

        return response
