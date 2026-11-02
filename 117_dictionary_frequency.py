# Question 10: Write a Python program to count
# the frequency of each character in a string
# using a dictionary.

text = "hello"

frequency = {}

for char in text:

    if char in frequency:

        frequency[char] += 1

    else:

        frequency[char] = 1

print("Character Frequency:", frequency)