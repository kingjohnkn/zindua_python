import re

def extract_phone_numbers(string):
    # Define the regular expression pattern
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    # Use the findall function to extract all phone numbers from the string
    phone_numbers = re.findall(pattern, string)
    # Return the list of phone numbers
    return phone_numbers

def extract_email_addresses(string):
    # Define the regular expression pattern
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    # Use the findall function to extract all email addresses from the string
    email_addresses = re.findall(pattern, string)
    # Return the list of email addresses
    return email_addresses

def replace_email_addresses(string, replacement):
    # Define the regular expression pattern
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    # Use the sub function to replace all email addresses in the string with the replacement string
    replaced_string = re.sub(pattern, replacement, string)
    # Return the modified string
    return replaced_string


string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"

print(extract_phone_numbers(string))
print(extract_email_addresses(string))
print(replace_email_addresses(string, 'john@gmail.com'))
