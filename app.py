# from crypt import methods
# from multiprocessing import connection
# from flask import Flask, redirect, render_template, request, session, url_for
# from utils import get_book, get_book_2,one_name
# from models import Book
# from db_utils import get_db_connection, get_session

import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from variables import URI_DB


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = URI_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

