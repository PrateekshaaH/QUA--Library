# QUA Library Management System
 
A desktop library management app built with Python (Tkinter) and MySQL.
 
## Features
- Admin login
- Add, search, view, and delete books
- Issue and return books
- View members and borrowing records
- Graphs: top borrowed books, genre split, monthly trend, membership distribution
## Tech Stack
Python, Tkinter, MySQL, Matplotlib
 
## Setup
```
pip install mysql-connector-python matplotlib
```
Create a MySQL database `library_db` with `books`, `members`, and `book_records` tables. Update the credentials in `connect_db()` inside `library_app.py`, then run:
```
python library_app.py
```
 
## Login
Username: `admin` | Password: `admin123
