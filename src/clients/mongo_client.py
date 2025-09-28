import pymongo
from pymongo import AsyncMongoClient

from ..config.config import get_settings

client = AsyncMongoClient(get_settings().mongodb_url, server_api=pymongo.server_api.ServerApi(version="1", strict=True,deprecation_errors=True))