# from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine

from datetime import datetime

# from variables import URI_DB
from app import db
# base = declarative_base()

# class Book(base):
class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    author =  db.Column(db.String(100), nullable = False)
    created = db.Column(db.DateTime, default = datetime.now)
    updated = db.Column(db.DateTime, default = datetime.now, onupdate = datetime.now)

# engin = create_engine(URI_DB)
# base.metadata.create_all(engin)