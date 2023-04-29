phonebook = {}


def add_contact(name, number):
    if name in phonebook:
        print('Error: Contact already exists.')
    else:
        phonebook[name] = number
        print('Contact added.')


def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print('Contact deleted.')
    else:
        print('Error: Contact not found.')


def search_contact(name):
    if name in phonebook:
        print('Phone number:', phonebook[name])
    else:
        print('Error: Contact not found.')


def print_contacts():
    if phonebook:
        print('Contacts:')
        for name, number in phonebook.items():
            print(name + ':', number)
    else:
        print('No contacts.')


def main():
    while True:
        print('Choose an option:')
        print('1. Add a contact')
        print('2. Delete a contact')
        print('3. Search for a contact')
        print('4. Print all contacts')
        print('5. Quit')

        choice = input('> ')

        if choice == '1':
            name = input('Enter contact name: ')
            number = input('Enter phone number: ')
            add_contact(name, number)

        elif choice == '2':
            name = input('Enter contact name: ')
            delete_contact(name)

        elif choice == '3':
            name = input('Enter contact name: ')
            search_contact(name)

        elif choice == '4':
            print_contacts()

        elif choice == '5':
            print('Goodbye!')
            break

        else:
            print('Invalid choice. Try again.')


if __name__ == '__main__':
    main()
