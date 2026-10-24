# libs
import pickle
import os

# PATH
PATH = "C:/Users/Amir/Desktop/Library-Management/data/"

# validation


def checkFileExists():
    if not os.path.exists(PATH + "users.dat"):
        f = open(PATH + "users.dat", "wb")
        usersdict = {}
        pickle.dump(usersdict, f)

    if not os.path.exists(PATH + "books.dat"):
        f = open(PATH + "books.dat", "wb")
        booksdict = {}
        pickle.dump(booksdict, f)

    if not os.path.exists(PATH + "borrows.dat"):
        f = open(PATH + "borrows.dat", "wb")
        borrowsdict = {}
        pickle.dump(borrowsdict, f)


# functions


def add_user(name, family, father_name, code, birthday):
    checkFileExists()

    f = open(PATH + "users.dat", "rb")
    users_dict = pickle.load(f)
    f.close()

    user_id = len(users_dict)
    users_dict[user_id] = [name, family, father_name, code, birthday]

    f = open(PATH + "users.dat", "wb")
    pickle.dump(users_dict, f)
    f.close()
    print("user aded successfully with library code : ", user_id)


def add_book(title, author, subject, year):
    checkFileExists()
    f = open(PATH + "books.dat", "rb")
    books_dict = pickle.load(f)
    f.close()
    books_dict[title] = [author, subject, year]

    f = open(PATH + "books.dat", "wb")
    pickle.dump(books_dict, f)
    f.close()


def search_book(title):
    f = open(PATH + "books.dat", "rb")
    books_dict = pickle.load(f)
    f.close()
    if title in books_dict:
        print(books_dict[title])


def borrow(user_id, title):
    checkFileExists()
    f = open(PATH + "borrows.dat", "rb")
    borrowsdict = pickle.load(f)
    f.close()
    borrowsdict[user_id] = title

    f = open(PATH + "borrows.dat", "wb")
    pickle.dump(borrowsdict, f)
    f.close()


def show_all():
    f = open(PATH + "users.dat", "rb")
    usersdict = pickle.load(f)
    f.close()

    f = open(PATH + "books.dat", "rb")
    booksdict = pickle.load(f)
    f.close()

    f = open(PATH + "borrows.dat", "rb")
    borrowsdict = pickle.load(f)
    f.close()

    print(usersdict)
    print("-------------------------------------------------------------")
    print(booksdict)
    print("-------------------------------------------------------------")
    print(borrowsdict)


# Start

ch = 1
while ch != 0:
    print(
        "===============================================================Library==============================================================="
    )
    print(
        "1-Add User\n2-Add New Book\n3-Search Book\n4-Borrow\n5-Show All info\n0-Exit"
    )
    ch = int(input("Enter Choice:"))
    os.system("cls")
    if ch == 1:
        name = input("Enter Name:")
        family = input("Enter Family:")
        father_name = input("Enter Father Name:")
        code = input("Enter Nationality Code:")
        birthday = input("Enter Birthday:")
        add_user(name, family, father_name, code, birthday)

    if ch == 2:
        title = input("Enter Title:")
        author = input("Enter Author:")
        subject = input("Enter Subject:")
        year = input("Enter Year:")
        add_book(title, author, subject, year)

    if ch == 3:
        title = input("Enter Title:")
        search_book(title)

    if ch == 4:
        user_id = input("Enter User Id:")
        title = input("Enter Title:")
        borrow(user_id, title)

    if ch == 5:
        show_all()
