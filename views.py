from flask import render_template, request,redirect, url_for
from app import db, app
from models import Book
from utils import get_book

from sqlalchemy import or_
from webargs import fields
from webargs.flaskparser import use_kwargs

# s = get_session()

@app.route("/")
def index():
    return render_template('index.html')


# @app.route("/books/list")
# def list_book():
#     connection = get_db_connection()
#     books_in = connection.execute('SELECT * FROM books;').fetchall()
#     connection.close()
#     return render_template('books/list.html', books1 = books_in) 

@app.route("/books/list")
def list_book():
    # books_in = s.query(Book).all()
    books_in = Book.query.all()
    return render_template('books/list.html', books1 = books_in) 
    
# @app.route('/books/detail/<int:book_id>')
# def detail_book(book_id):
#     connection = get_db_connection()
#     book_detail = get_book(book_id, connection)
#     return render_template('books/detail.html', book1 = book_detail)

@app.route('/books/detail/<int:book_id>')
def detail_book(book_id):
    # book_detail = get_book_2(book_id, s, Book)
    book_detail = get_book(book_id)
    return render_template('books/detail.html', book1 = book_detail)

# @app.route('/books/create', methods=['GET', 'POST'])
# def create_book():
    
#     if request.method == 'POST':
#         title = request.form['title']
#         author = request.form['author']

#         if title and author:
#             connection = get_db_connection()
#             connection.execute('INSERT INTO books (title, author) VALUES (?,?)', (title, author) )
#             connection.commit()
#             connection.close()
#             return redirect (url_for('list_book'))
#     return render_template ('books/create.html')
@app.route('/books/create', methods=['GET', 'POST'])
def create_book():
    
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        if title and author:
            book = Book(title=title , author=author)
            db.session.add(book)
            db.session.commit()
            return redirect (url_for('list_book'))
    return render_template ('books/create.html')

# @app.route('/books/edit/<int:book_id>', methods = ['GET', 'POST'])
# def update_book(book_id):
#     connection = get_db_connection()
#     book_detail = get_book(book_id, connection)

#     if request.method == 'POST':
#         title = request.form ['title']
#         author = request.form['author']
#         if title and author:
#             connection = get_db_connection()
#             connection.execute('update books set title=?, author=? where id=?', (title, author, book_id) )
#             connection.commit()
#             connection.close()
#             return redirect (url_for('list_book'))
#     return render_template ('books/update.html', book1=book_detail)
@app.route('/books/edit/<int:book_id>', methods = ['GET', 'POST'])
def update_book(book_id): 
    # book_detail = get_book_2(book_id, s, Book)
    book_detail = get_book(book_id)

    if request.method == 'POST':
        title = request.form ['title']
        author = request.form['author']
        if title and author:
            book_detail.title = title
            book_detail.author = author
            db.session.add(book_detail)
            db.session.commit()
            return redirect (url_for('list_book'))
    return render_template ('books/edit.html', book1=book_detail)

# @app.route('/books/delete/<int:book_id>', methods = ['POST', 'GET'])
# def delete_book(book_id):
    
#     if request.method == 'POST':
#         connection = get_db_connection()
#         connection.execute('DELETE FROM books WHERE id = ?', (book_id,))
#         connection.commit()
#         connection.close()
#         return redirect (url_for('list_book'))
@app.route('/books/delete/<int:book_id>', methods = ['GET','POST'])
def delete_book(book_id):
    # book_detail = get_book_2(book_id, s, Book)
    book_detail = get_book(book_id)
    if request.method == 'POST':
        db.session.delete(book_detail)
        db.session.commit()
        return redirect (url_for('list_book'))
    else:
        return render_template ('books/delete.html', book1=book_detail) 

# @app.route('/unique_name')
# def one():
#     book = one_name(s, Book)
#     return book

@app.route('/book/search')
@use_kwargs(
    {
        "value": fields.Str(required=True)
    },
    location = 'query'
)
def search_book(value):
    """
    SELECT * FROM books WHERE title='' OR author='';
    """
    books_in = Book.query.filter(or_(Book.title == value, Book.author == value)).all()

    return render_template('books/search.html', books1 = books_in)

if __name__ == "__main__":
    app.run(debug=True, port=5000) 