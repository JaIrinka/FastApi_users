from .user import user
from .base import metadata, engine

metadata.create_all(bind=engine)