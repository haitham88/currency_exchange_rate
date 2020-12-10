from fastapi import APIRouter, Depends, Response
from app.api.currency_apis import CurrencyAPI
from app.middlewares.api_decorators import date_validation
import json

router = APIRouter()


@router.get("/rate")
def exchange_currency(from_currency: str, to_currency: str, validation_result: dict = Depends(date_validation)):
    if validation_result.status:
        currency_api = CurrencyAPI()
        date = validation_result.data.get("date")
        exchange_currency_response = currency_api.exchange_currency(from_currency, to_currency, date)

        return Response(content=json.dumps(exchange_currency_response.data), status_code=exchange_currency_response.status_code)
    else:
        return Response(content=json.dumps(validation_result.data), status_code=validation_result.status_code)
