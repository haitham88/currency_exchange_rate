from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
from app import settings
from app.utils.exceptions import Exceptions


class Mysql(object):

    def __init__(self):
        try:
            self.SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{}:{}@{}:3306/{}"
            self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL.format(settings.DATABASE_USERNAME,
                                                                        settings.DATABASE_PASSWORD,
                                                                        settings.DATABASE_HOST,
                                                                        settings.DATABASE_NAME))
            self.sessionLocal = sessionmaker(bind=self.engine)
            self.exceptions = Exceptions()

        except Exception as e:
            exception = self.exceptions.get_exception("connecting_database")
            print(exception)
