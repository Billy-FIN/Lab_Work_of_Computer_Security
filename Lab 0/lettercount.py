#!/usr/bin/env python3
import sys


# Read the input from stdin
data = ''
for line in sys.stdin:
    data = data + line
    if line == '':
        break
data = ''.join([i for i in data if i.isalpha()])
data = data.lower()

letters = {}
for letter in data:
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] += 1
# Sort the dictionary by key
order = sorted(letters)
for letter in order:
    value = letters[letter]
    print(f'{letter} {value}')
