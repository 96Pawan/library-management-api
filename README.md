# Django Book Management API

This project is a Django-based API for managing books in a library. It allows users to add, view, update, delete books, and also borrow and return them via a REST API.

## Setup and Run Instructions

### 1. Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/96Pawan/library-management-api.git

##2. Create a Virtual Environment
Create a virtual environment for the project:

```bash
python -m venv venv
Activate the virtual environment:

```bash
venv\Scripts\activate


##3. Install Dependencies
Install the necessary dependencies:

```bash
pip install -r requirements.txt

##4. Apply Migrations
Run the following command to apply database migrations:

```bash
python manage.py migrate

##5. Run the Server
Start the Django development server:

```bash
python manage.py runserver

Your API should now be running at http://127.0.0.1:8000/.



#### API Endpoints

The API exposes the following endpoints:

### 1. GET /api/books/
Fetch a list of all books in the library.

Example Request:

GET /api/books/
we have implemented filter you search based on filters
Example Response:

json
[
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic Fiction",
        "publication_year": 1925,
        "is_borrowed": false,
        "borrower_name": null,
        "borrow_date": null
    },
    ...
]

### 2. POST /api/books/
Add a new book to the library.

Example Request:

POST /api/books/
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "genre": "Classic Fiction",
  "publication_year": 1925,
  "is_borrowed": false,
  "borrower_name": null,
  "borrow_date": null
}

Example Response:

json
{
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Classic Fiction",
    "publication_year": 1925,
    "is_borrowed": false,
    "borrower_name": null,
    "borrow_date": null
}

###  3. GET /api/books/{id}/
Fetch details of a specific book by ID.

Example Request:

GET /api/books/1/

Example Response:

json
{
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Classic Fiction",
    "publication_year": 1925,
    "is_borrowed": false,
    "borrower_name": null,
    "borrow_date": null
}

### 4. PUT /api/books/{id}/
Update the details of a specific book.

Example Request:

PUT /api/books/1/
{
  "title": "The Great Gatsby Updated",
  "author": "F. Scott Fitzgerald",
  "genre": "Classic Fiction",
  "publication_year": 1925,
  "is_borrowed": true,
  "borrower_name": "Sarah Smith",
  "borrow_date": "2024-12-05"
}

### 5. DELETE /api/books/{id}/
Delete a specific book by ID.

Example Request:

DELETE /api/books/1/

### 6. POST /api/books/{id}/borrow/
Borrow a book. Marks the book as borrowed and updates the borrower name and borrow date.

Example Request:

POST /api/books/1/borrow/
{
  "borrower_name": "John Doe",
  "borrow_date": "2024-12-10"
}

Example response :
1. If no one borrowed the book

{
    "success": "Book 'The Great Gatsby' has been borrowed successfully."
}

2. If anyone had already borrowed the book it shows 

{
    "error": "Book is already borrowed."
}

### 7. POST /api/books/{id}/return/
This api helps to return the book from borrower

Example Request:

POST /api/books/2/borrow/
{}
After clicking on POST in DRF

1.If someone had borrowed the book then it shows,

{
    "success": "Book 'The Great Gatsby' has been returned successfully."
}

2.If no one had borrowed the book then it shows,

{
    "error": "Book is not currently borrowed."
}
