import csv

def read_books(filename):
    books = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append(row)
    return books

def search_by_author(books, author):
    result = []
    for book in books:
        if book['author'] == author:
            result.append(book)
    return result

def search_by_isbn(books, isbn):
    for book in books:
        if book['ISBN'] == isbn:
            return book['title'], book['price']
    return None

def search_by_price_range(books, min_price, max_price):
    result = []
    for book in books:
        if min_price <= float(book['price']) <= max_price:
            result.append(book)
    return result

def add_book(filename, title, author, isbn, price):
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([title, author, isbn, price])

def main():
    filename = 'books.csv'
    books = read_books(filename)

    while True:
        print('Choose an option:')
        print('1. Search by author')
        print('2. Search by ISBN')
        print('3. Search by price range')
        print('4. Add a new book')
        print('5. Quit')

        choice = input('> ')

        if choice == '1':
            author = input('Enter author name: ')
            result = search_by_author(books, author)
            if result:
                for book in result:
                    print(book['title'], book['author'], book['ISBN'], book['price'])
            else:
                print('No results found.')

        elif choice == '2':
            isbn = input('Enter ISBN: ')
            result = search_by_isbn(books, isbn)
            if result:
                title, price = result
                print(title, price)
            else:
                print('No results found.')

        elif choice == '3':
            min_price = float(input('Enter minimum price: '))
            max_price = float(input('Enter maximum price: '))
            result = search_by_price_range(books, min_price, max_price)
            if result:
                for book in result:
                    print(book['title'], book['author'], book['ISBN'], book['price'])
            else:
                print('No results found.')

        elif choice == '4':
            title = input('Enter title: ')
            author = input('Enter author: ')
            isbn = input('Enter ISBN: ')
            price = float(input('Enter price: '))
            add_book(filename, title, author, isbn, price)
            print('Book added.')

        elif choice == '5':
            print('Goodbye!')
            break

        else:
            print('Invalid choice. Try again.')