import csv

# List of books with their information
books = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald',
        'ISBN': '9780141182636', 'price': 10.99},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee',
        'ISBN': '9780061120084', 'price': 12.99},
    {'title': '1984', 'author': 'George Orwell',
        'ISBN': '9780451524935', 'price': 8.99},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen',
        'ISBN': '9780141439518', 'price': 9.99},
]

# Open a new CSV file in write mode
with open('books.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Title', 'Author', 'ISBN', 'Price'])

    # Write the data rows
    for book in books:
        writer.writerow([book['title'], book['author'],
                        book['ISBN'], book['price']])
