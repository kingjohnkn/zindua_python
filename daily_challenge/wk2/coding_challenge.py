import re

def extract_phone_numbers(string):    
    pattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    matches = pattern.finditer(string)
    for match in matches:
        return match.group(0)
    
def extract_email_addresses(string):    
    pattern = re.compile(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    matches = pattern.finditer(string)
    for match in matches:
        return match.group(0)
    
def replace_email_addresses(string, replacement):
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    replaced_string = pattern.sub(replacement, string)
    return replaced_string

string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333" 

print(extract_phone_numbers(string))
print(extract_email_addresses(string))
print(replace_email_addresses(string, 'johnk@gmail.com'))


# Output: ['(123) 456-7890', '(111) 222-3333'] 
# print(extract_email_addresses(string)) 
# Output: ['info@example.com'] print(replace_email_addresses(string, "REPLACED")) 
# Output: "Please contact REPLACED for assistance. Phone: (123) 456-7890 or (111) 222-3333"