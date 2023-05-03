# Check for Palindrome words

### A Palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.

In this code, 
```
def is_palindrome(word):
return word == word[::-1]


with open('words_in_english_dictionary.txt', 'r') as file:
    palindrome = []
    for line in file:
        for word in line.split():
            if is_palindrome(word):
                palindrome.append(word)
                # print(word)

with open('palindromes.txt', 'a+') as file2:
    for word in palindrome:
        file2.writelines(word + '\n')

```
The ```is_palindrome``` function checks if a given word is a palindrome by comparing the word to its reverse. 

The ```with open``` statement opens the file in ```read``` mode and automatically closes it when the code inside the block is done executing. 

The for loop reads each line in the file, splits the line into words, and then checks if each word is a palindrome using the ```is_palindrome``` function. If a word is a palindrome, it is added (append) to the empty list created before the for loop begins.

Once all the palindromes from the file have been added to the ```palindrome``` list, create a file ```palindromes.txt``` using the ```a+``` mode in the ```with open``` statement. 

The ```a+``` mode opens the file for both appending and reading. The file pointer is placed at the end of the file, so new content is added after the existing content. If the file does not exist, it is created.

The final for loop loops around the list appending all the words in the list to the file. The ```+ '\n'``` at the end of ```word``` ensures that each word in the list is placed on a new line in the file ```palindrome.txt```.