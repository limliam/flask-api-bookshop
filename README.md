## Flask API Bookstore

# Description

The Flask Bookstore App consists of two Flask applications: 

1. flask-api-bookshop. a REST API for managing a bookstore's data and a client web app for interacting with the API to perform CRUD operations on the book data. The API app provides endpoints for CRUD operations on books using SQLite as the database backend. 

2. flask-bookshop. The web app consumes these API endpoints to display, add, edit, and delete books through a user-friendly interface. this app is in a separate project 


# How to Create and Install the App
1. Clone the Repository
git clone <github url>
cd flask-api-bookstore

2. Set Up Virtual Environment
python3 -m venv venv

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate
. venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Create SQLite Database
Create a file named books.db in the project directory.

5. Run the Flask App
python app.py --> this command is deprecated. 

Instead use this:
flask run ( this will run on 5000 by default)

The app should now be running on http://localhost:5000/.

When running the client app, because the api is on 5000, you want the client on different port, e.g. 5001. 
flask run --port=5001 

# How to Test API Using Curl

1. Retrieve All Books
curl http://127.0.0.1:5000/books

2. Retrieve a Specific Book
curl http://localhost:5000/books/<book_id>
Replace <book_id> with the actual ID of the book.

3. Add a New Book
curl -X POST -H "Content-Type: application/json" -d '{"isbn":"1234567890","title":"Blood Meridian","author":"Cormac McCarthy","publisher":"Picador","year":1985}' http://127.0.0.1:5000/books

curl -X POST -H "Content-Type: application/json" -d '{"isbn":"234567898","title":"To Kill a Mockingbird","author":"Harper Lee","publisher":"Vintage","year":2004}' http://127.0.0.1:5000/books

4. Update an Existing Book
curl -X PUT -H "Content-Type: application/json" -d '{"isbn":"1234567890","title":"Blood Meridian","author":"Cormac McCarthy","publisher":"Picador B","year":1985}' http://127.0.0.1:5000/books/<book_id>
Replace <book_id> with the actual ID of the book.

5. Delete an Existing Book
curl -X DELETE http://127.0.0.1:5000/books/<book_id>
Replace <book_id> with the actual ID of the book.



# Contributing
Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.