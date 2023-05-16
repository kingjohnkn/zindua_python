import json


def parse_file(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    lines = file_contents.split("\n")
    name_address_list = [line.split(", ") for line in lines]
    address_book = {}
    for name_address in name_address_list:
        name = name_address[0]
        address = name_address[1] + ", " + name_address[2]
        address_book[name] = address
    return address_book


file_path = "name_address.txt"
address_book = parse_file(file_path)
print(address_book)
json_object = json.dumps(address_book, indent=4)
print(json_object)
