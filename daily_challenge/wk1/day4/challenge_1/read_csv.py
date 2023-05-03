import csv


def read_books_csv(filename):
    books = []
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append(row)
    return books


def search_books_by_author(author, books):
    # books = []
    # for book in books:
    #     if book['Author'] == author:
    #         return book
    
    return [book for book in books if book['Author'] == author]


def search_book_by_isbn(isbn, books):
    for book in books:
        if book['ISBN'] == isbn:
            return {'Title': book['Title'], 'Price': book['Price']}
    return None


def search_books_by_price_range(min_price, max_price, books):
    return [book for book in books if min_price <= float(book['Price']) <= max_price]


def add_book_to_csv(book, filename):
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Title', 'Author', 'ISBN', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(book)


def main():
    filename = 'books.csv'
    books = read_books_csv(filename)
    while True:
        print('Search for books by author, ISBN, or price range')
        print('1. Search by author')
        print('2. Search by ISBN')
        print('3. Search by price range')
        print('4. Add a book')
        print('5. Quit')
        choice = input('Enter your choice (1-5): ')
        if choice == '1':
            author = input('Enter author name: ')
            results = search_books_by_author(author, books)
            if results:
                for book in results:
                    print(book['Title'])
            else:
                print('No books found.')
        elif choice == '2':
            isbn = input('Enter ISBN: ')
            result = search_book_by_isbn(isbn, books)
            if result:
                print(result['Title'], result['Price'])
            else:
                print('No book found.')
        elif choice == '3':
            min_price = float(input('Enter minimum price: '))
            max_price = float(input('Enter maximum price: '))
            results = search_books_by_price_range(min_price, max_price, books)
            if results:
                for book in results:
                    print(book['Title'])
            else:
                print('No books found.')
        elif choice == '4':
            title = input('Enter book title: ')
            author = input('Enter author name: ')
            isbn = input('Enter ISBN: ')
            price = input('Enter price: ')
            new_book = {'Title': title, 'Author': author,
                        'ISBN': isbn, 'Price': price}
            add_book_to_csv(new_book, filename)
            print('Book added to CSV file.')
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()