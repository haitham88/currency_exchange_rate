import os
from dotenv import load_dotenv

PROJECT_ROOT = os.path.abspath(os.path.join(__file__, os.pardir))
load_dotenv(os.path.join(PROJECT_ROOT, '.env'))

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')
EXCHANGE_CURRENCY_API_PREFIX = os.getenv("EXCHANGE_CURRENCY_API_PREFIX")
