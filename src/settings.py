from starlette.config import Config
from starlette.datastructures import URL, Secret


config = Config('.env')

DEBUG = config('DEBUG', cast=bool, default=True)

DB_HOST = config('DB_HOST', cast=URL, default='localhost')
DB_PORT = config('DB_PORT', cast=int, default='27017')
DB_USERNAME = config('DB_USERNAME', cast=Secret)
DB_PASSWORD = config('DB_PASSWORD', cast=Secret)

AUTH_METHOD = config('AUTH_ALGORITHM', cast=str, default='HS256')
AUTH_KEY = config('AUTH_KEY', cast=Secret)
