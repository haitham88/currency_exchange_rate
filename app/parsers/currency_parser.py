

def currency_rate_repository_parser(currency_rate):
    return {
        "from_currency": currency_rate.from_currency,
        "to_currency": currency_rate.to_currency,
        "date": currency_rate.date,
        "rate": currency_rate.rate
    }

def currency_rate_gateway_parser(currency_rate):
     rates = currency_rate.get("rates")
     for key, value in rates.items():
         to_currency = key
         rate = value

     return {
        "from_currency": currency_rate.get("base"),
        "to_currency": to_currency,
        "date": currency_rate.get("date"),
        "rate": rate
    }