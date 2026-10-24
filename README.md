# Library Management System

A simple library management system built with Python.

## Features

- Add library members
- Add new books
- Search for books by title
- Record book borrowing
- Display stored library information
- Save data using Python's `pickle` module

## Technologies

- Python
- Pickle
- OS module

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project directory in your terminal.
4. Run:

```bash
python main.py
```

## Note

This is a beginner Python project created for learning file handling, dictionaries, functions, and basic application logic.

## Demo

### 1. Adding a New Member

```text
Enter Choice: 1
Enter Name: Amir
Enter Family: Ahmadi
Enter Father Name: Reza
Enter Nationality Code: 1234567890
Enter Birthday: 1385/05/12

user aded successfully with library code : 0
```

### 2. Adding a New Book

```text
Enter Choice: 2
Enter Title: Python Basics
Enter Author: John Smith
Enter Subject: Programming
Enter Year: 2024
```

The book is saved successfully in the library database.

### 3. Searching for a Book

```text
Enter Choice: 3
Enter Title: Python Basics

['John Smith', 'Programming', '2024']
```

### 4. Borrowing a Book

```text
Enter Choice: 4
Enter User Id: 0
Enter Title: Python Basics
```

The borrowing record is saved successfully.

### 5. Showing All Information

```text
Enter Choice: 5

{0: ['Amir', 'Ahmadi', 'Reza', '1234567890', '1385/05/12']}

-------------------------------------------------------------

{'Python Basics': ['John Smith', 'Programming', '2024']}

-------------------------------------------------------------

{'0': 'Python Basics'}
```

### 6. Exiting the Program

```text
Enter Choice: 0
```

The program exits.

## Data Storage

The application stores data locally using Python's `pickle` module:

- `users.dat` — Library members
- `books.dat` — Book records
- `borrows.dat` — Borrowing records

## Disclaimer

All names, identification numbers, and other personal details shown in this demo are fictional examples. Actual output may vary depending on the data stored in the application.