import sqlite3
from variables import DN_NAME, URI_DB
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import base

def get_db_connection():
    connection = sqlite3.connect(DN_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def get_session():
    engin = create_engine(URI_DB)
    base.metadata.bind = engin
    db_session = sessionmaker(bind = engin)
    return db_session()
