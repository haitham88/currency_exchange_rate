from app.models.currency_rate import CurrencyRate
from .base_repository import BaseRepository


class CurrencyRepository(BaseRepository):
    def __init__(self, session, exceptions):
        super().__init__(session, exceptions)

    def get(self, **kwargs):
        try:
            currency_rate_result = self.session.query(CurrencyRate).filter(CurrencyRate.from_currency == kwargs.get("from_currency"),
                                                                    CurrencyRate.to_currency == kwargs.get("to_currency"),
                                                                    CurrencyRate.date == kwargs.get("date")).first()
            return currency_rate_result
        except Exception as e:
            exception = self.exceptions.get_exception("getting_data_from_db", e)
            print(exception)


    def create(self, **kwargs):
        try:
            exchange_rate = CurrencyRate()
            exchange_rate.from_currency = kwargs.get("from_currency")
            exchange_rate.to_currency = kwargs.get("to_currency")
            exchange_rate.date = kwargs.get("date")
            exchange_rate.rate = kwargs.get("rate")
            self.session.add(exchange_rate)
            self.session.commit()
        except Exception as e:
            print(e)