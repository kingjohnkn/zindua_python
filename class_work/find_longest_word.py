def find_longest_word(sentence):
    """
    A function that takes a sentence and returns the longest word.
    """
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

sentence = "A function that takes a sentence and returns the longest word."

print(find_longest_word(sentence))