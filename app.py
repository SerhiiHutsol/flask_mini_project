from crypt import methods
from multiprocessing import connection
import sqlite3
from variables import URL
from flask import Flask, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect(URL)
    connection.row_factory = sqlite3.Row
    return connection

def get_book(book_id):
    connection = get_db_connection()
    book = connection.execute('SELECT * FROM books WHERE id = ?', (book_id, )).fetchone()
    connection.close()
    if book is None:
        abort (404)
    else:
        return book

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/books/list")
def list_book():
    connection = get_db_connection()
    books_in = connection.execute('SELECT * FROM books;').fetchall()
    connection.close()
    return render_template('books/list.html', books1 = books_in) 
    
@app.route('/books/detail/<int:book_id>')
def detail_book(book_id):
    book_detail = get_book(book_id)
    return render_template('books/detail.html', book1 = book_detail)

@app.route('/books/create', methods=['GET', 'POST'])
def create_book():
    
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        if title and author:
            connection = get_db_connection()
            connection.execute('INSERT INTO books (title, author) VALUES (?,?)', (title, author) )
            connection.commit()
            connection.close()
            return redirect (url_for('list_book'))
    return render_template ('books/create.html')

@app.route('/books/edit/<int:book_id>', methods = ['GET', 'POST'])
def update_book(book_id):

    book_detail = get_book(book_id)

    if request.method == 'POST':
        title = request.form ['title']
        author = request.form['author']
        if title and author:
            connection = get_db_connection()
            connection.execute('update books set title=?, author=? where id=?', (title, author, book_id) )
            connection.commit()
            connection.close()
            return redirect (url_for('list_book'))
    return render_template ('books/update.html', book1=book_detail)

@app.route('/books/delete/<int:book_id>', methods = ['POST', 'GET'])
def delete_book(book_id):
    
    if request.method == 'POST':
        connection = get_db_connection()
        connection.execute('DELETE FROM books WHERE id = ?', (book_id,))
        connection.commit()
        connection.close()
        return redirect (url_for('list_book'))

app.run(debug=True, port=5000)