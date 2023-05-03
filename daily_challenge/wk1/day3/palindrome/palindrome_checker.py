def is_palindrome(word):
    return word == word[::-1]


with open('words_in_english_dictionary.txt', 'r') as file:
    palindrome = []
    for line in file:
        for word in line.split():
            if is_palindrome(word):
                palindrome.append(word)
                # print(word)


# print(palindrome)

with open('palindromes.txt', 'a+') as file2:
    for line in palindrome:
        file2.writelines(line + '\n')
