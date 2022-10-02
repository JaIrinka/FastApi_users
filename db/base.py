from sqlalchemy import create_engine, MetaData
from app.config import DB_URL

metadata = MetaData()
engine = create_engine(
    DB_URL
)
