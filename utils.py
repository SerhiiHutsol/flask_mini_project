
from models import Book
from werkzeug.exceptions import abort
import requests
 

# def get_book(book_id, connection):
#     book = connection.execute('SELECT * FROM books WHERE id = ?', (book_id, )).fetchone()
#     connection.close()
#     if book is None:
#         abort (404)
#     else:
#         return book

def get_book(book_id):
    book = Book.query.filter_by(id = book_id).one()
    if book is None:
        abort (404)
    else:
        return book

def get_book_2(book_id, session, model):
    book= session.query(model).filter_by(id = book_id).one()
    if book is None:
        abort (404)
    else:
        return book

def one_name( session, model):
    book_one = session.query(model).group_by().row.title
    result = session.query(model).all()
    for i in result:
        print('title ;', i.title )

def search_btc(mark):
    response = requests.get('https://bitpay.com/api/rates')
    data = response.json()
    for i in range(len(data)):
        a = data[i]
        a.get('code')
        # print(a)
        if a.get('code').lower() == mark.lower():
            res = a.get('rate')
            res1 = a.get('name')
            return f'{res} {res1}'
        # else:
        #     return print(f'Not found {mark}')
    

# print(search_btc('BND'))