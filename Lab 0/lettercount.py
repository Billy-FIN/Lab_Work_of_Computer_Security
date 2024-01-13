import os

def lettercount(filename):
    # Check if file exists
    if not os.path.exists(filename):
        return "File not found"
    with open(filename, 'r') as file:
        data = file.read()
    # Remove all non-alphabetic characters
    data = ''.join([i for i in data if i.isalpha()])
    # all letters to lowercase
    data = data.lower()
    letters = {}
    for letter in data:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    # Sort the dictionary by key
    order = sorted(letters)
    output(order, letters, filename)

def output(order, letters, filename):
    with open(filename[:-4] + '-out.txt', 'w') as file:
        for letter in order:
            value = letters[letter]
            file.write(f'{letter} {value}\n')

if __name__ == '__main__':
    lettercount('test2.txt')

