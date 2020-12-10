from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()
class CurrencyRate(Base):
    __tablename__ = "exchange_currency_rates"

    id = Column(Integer, primary_key=True, index=True)
    from_currency = Column(String)
    to_currency = Column(String)
    date = Column(String)
    rate = Column(Float)


