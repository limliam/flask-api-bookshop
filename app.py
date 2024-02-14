from flask import Flask, jsonify, request, abort
import sqlite3

app = Flask(__name__)

# Database initialization
DATABASE = 'books.db'

def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publisher TEXT NOT NULL,
            year INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Routes for CRUD operations
@app.route('/books', methods=['GET'])
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return jsonify([dict(book) for book in books])

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()
    conn.close()
    if book is None:
        abort(404)
    return jsonify(dict(book))

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    isbn = data.get('isbn')
    title = data.get('title')
    author = data.get('author')
    publisher = data.get('publisher')
    year = data.get('year')
    if not isbn or not title or not author or not publisher or not year:
        abort(400)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (isbn, title, author, publisher, year) VALUES (?, ?, ?, ?, ?)',
                   (isbn, title, author, publisher, year))
    conn.commit()
    book_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': book_id}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    isbn = data.get('isbn')
    title = data.get('title')
    author = data.get('author')
    publisher = data.get('publisher')
    year = data.get('year')
    if not isbn or not title or not author or not publisher or not year:
        abort(400)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET isbn = ?, title = ?, author = ?, publisher = ?, year = ? WHERE id = ?',
                   (isbn, title, author, publisher, year, book_id))
    conn.commit()
    conn.close()
    return '', 204

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
    return '', 204

if __name__ == '__main__':
    create_database()
    app.run(debug=True)



# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Sample data (for demonstration purposes)
# books = [
#     {"id": 1, "title": "Book 1", "isbn": "1234567890", "author": "Author 1", "publisher": "Publisher 1", "published_year": 2020},
#     {"id": 2, "title": "Book 2", "isbn": "0987654321", "author": "Author 2", "publisher": "Publisher 2", "published_year": 2019}
# ]

# # Routes
# @app.route('/books', methods=['GET'])
# def get_books():
#     return jsonify(books)

# @app.route('/books/<int:book_id>', methods=['GET'])
# def get_book(book_id):
#     book = next((book for book in books if book['id'] == book_id), None)
#     if book:
#         return jsonify(book)
#     return jsonify({"message": "Book not found"}), 404

# @app.route('/books', methods=['POST'])
# def add_book():
#     data = request.json
#     new_book = {
#         "id": len(books) + 1,
#         "title": data['title'],
#         "isbn": data['isbn'],
#         "author": data['author'],
#         "publisher": data['publisher'],
#         "published_year": data['published_year']
#     }
#     books.append(new_book)
#     return jsonify(new_book), 201

# @app.route('/books/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     data = request.json
#     for book in books:
#         if book['id'] == book_id:
#             book.update(data)
#             return jsonify(book)
#     return jsonify({"message": "Book not found"}), 404

# @app.route('/books/<int:book_id>', methods=['DELETE'])
# def delete_book(book_id):
#     global books
#     books = [book for book in books if book['id'] != book_id]
#     return jsonify({"message": "Book deleted"})

# if __name__ == '__main__':
#     app.run(debug=True)
