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
