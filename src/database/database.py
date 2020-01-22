from pymongo import MongoClient
from src import settings

client = MongoClient(
    host=str(settings.DB_HOST),
    port=settings.DB_PORT,
    username=str(settings.DB_USERNAME),
    password=str(settings.DB_PASSWORD),
)

users_db = client.users

users_collection = users_db.users
