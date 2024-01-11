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


