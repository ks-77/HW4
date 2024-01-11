"""
HW4
Savchenko Kirill
"""

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
