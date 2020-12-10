import datetime

from app.utils.response import Response
from app.utils.constants_variables import HTTP_400_BAD_REQUEST
from app.utils.exceptions import Exceptions

exceptions = Exceptions()

def date_validation(date: str):
    response = Response()

    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        response.status = True
        response.data = {"date": date}
    except:
        response.status = False
        response.status_code = HTTP_400_BAD_REQUEST
        response.data = {"message": exceptions.get_exception("date_error")}

    return response


