from models import (Base, session,
                    Book, engine)
import datetime
import csv


def menu():
    while True:
        print('''
              \nProgramming Books
              \r1) Add book
              \r2) View all books
              \r3) Search for book
              \r4) Book Analaysis
              \r5) Exit''')
        choice = input('What would you like to do? > ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input('''
                  \rPlease choose one of the options above.
                  \rA number from 1-5.
                  \rPress enter to try again.''')
#main menu -add search, analysis, exit, view
# add books to the database
# edit books
#delete books
#search
#data cleaning

def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)


def clean_price(price_str):
    price_float = float(price_str)
    return int(price_float * 100)


    
def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)
            title = row[0]
            author = r[1]
            date = clean_date(row[2])
            price = clean_price(row[3])
            


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            #add book
            pass
        elif choice == '2':
            #view books
            pass
        elif choice =='3':
            #search
            pass
        elif choice =='4':
            #analysis
            pass
        else:
            print('Goodbye')
            app_running = False
            


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    #app()
    add_csv()
    