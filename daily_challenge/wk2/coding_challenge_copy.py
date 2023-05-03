import re


def extract_phone_numbers(string):
    # pattern = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
    # phone_numbers = pattern.findall(string)
    # return phone_numbers
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    phone_numbers = re.findall(pattern, string)
    return phone_numbers


def extract_email_addresses(string):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_addresses = re.findall(pattern, string)
    return email_addresses


def replace_email_addresses(string, replacement):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    replaced_string = re.sub(pattern, replacement, string)
    return replaced_string


string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"

print(extract_phone_numbers(string))
print(extract_email_addresses(string))
print(replace_email_addresses(string, 'john@gmail.com'))
