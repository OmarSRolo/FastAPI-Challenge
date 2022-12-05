from .base import get_settings
from data_layer.dbcontext import AlchemyDBContext
import databases

database = AlchemyDBContext(url_connection=get_settings().CONNECTION_STRING)
async_database = databases.Database(get_settings().CONNECTION_STRING)
