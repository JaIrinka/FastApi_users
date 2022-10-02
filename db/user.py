from sqlalchemy import Table, Column, Integer, String, DateTime
from .base import metadata
import datetime


user = Table(
    "user", metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("email", String, primary_key=True, unique=True),
    Column("name", String),
    Column("hashed_password", String),
    Column("created", DateTime, default=datetime.datetime.utcnow()),
    Column("updated", DateTime, default=datetime.datetime.utcnow())
)