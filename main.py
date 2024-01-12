"""
HW4
Savchenko Kirill
"""
import re
import string

# 1
sentence = input("Enter any sentence with letters and numbers: ")

letter_q = 0
number_q = 0

for symbol in sentence:
    if symbol.isalpha():
        letter_q += 1
    elif symbol.isdigit():
        number_q += 1
print(f"letters in text: {letter_q}")
print(f"numbers in text: {number_q}")

# 2

sentence = input("Enter any sentence: ")
find_sym = input("Enter the symbol you want to find: ")

print(sentence.count(find_sym))

# 3

sentence = input("Enter sentence: ")
word_original = input("Enter the word you want to change: ")
word_replace = input("Enter the word you want to replace the original with: ")

sentence = sentence.replace(word_original, word_replace)
print(sentence)

# 4

text = """Python is a programming language that lets you work more quickly and integrate your systems more effectively.
You can learn to use Python and see almost immediate gains in productivity and lower maintenance costs."""

print(text[2])     # if we are talking about the third in the text, and not in the output program
print(text[-2])
print(text[0: 5])
print(text[0: -2])
print(text[1:: 2])
print(text[2:: 2])
print(text[:: -1])
print(text[::-2])
print(len(text))

# additional task

text = """martha sees bananas are on sale! bananas are usually 3 dollars per bunch, but they are 1 dollar today.
 martha wants 3 bunches of bananas because she is going to make banana bread. this would normally cost Martha 9 dollars,
 but today it costs Martha 3 dollars. martha saved 6 dollars!"""

sentences = re.split(r'(?<=[.!?])\s+', text)

for sentence in sentences:
    print(sentence.capitalize())

"""
capitalized_sentences = [sentence.capitalize() for sentence in sentences]
result_text = ' '.join(capitalized_sentences)

print(result_text)
"""

print(f"number of \"!\": {text.count("!")}")

punctuation_count = sum(1 for char in text if char in string.punctuation)
print(f"number of punctuation mark: {punctuation_count}")

number_q = 0

for symbol in text:
    if symbol.isdigit():
        number_q += 1
print(number_q)
