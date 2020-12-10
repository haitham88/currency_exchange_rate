

class Exceptions:

    def get_exception(self, exception_key, error=None):
        exceptions = {
            "connecting_database": "couldn't connect to database with error: {}".format(error),
            "creating_new_row": "couldn't create new row to database with error: {}".format(error),
            "getting_data_from_db": "couldn't get data from database with error: {}".format(error),
            "getting_data_from_api": "couldn't get data from api with error: {}".format(error),
            "date_error": "Incorrect date format, should be YYYY-MM-DD"
        }

        return exceptions.get(exception_key, error)