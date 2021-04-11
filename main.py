# Case-Study #7 "Text Generator"
# Programmers:
# Alexander Zhuravlev (75%)
# Kremlin V. (25%)

import random


def control():
    """
    Function, checking input data.
    """
    try:
        n = int(input('Amount of sentences to generate: '))
        return n
    except ValueError:
        print('Integer number from 1 to 100 required. Please, try again.')
        exit()


def lists(filename):
    """
    Function, making lists and return them to main().
    """
    text = []
    keys = []
    connections = {}
    start_words = []
    try:
        with open(filename, 'r', encoding='UTF-8') as infile:
            for line in infile:
                for word in line.split():
                    text.append(word)
                    if word[0].isupper():
                        start_words.append(word)
        return text, keys, connections, start_words
    except FileNotFoundError:
        print('File "' + filename + '" was not found. Please, try again.')
        exit()


def check(text, keys, connections):
    for word in text:
        for j in range(len(text)):
            if text[j] == word:
                try:
                    keys.append(text[j + 1])
                except IndexError:
                    pass
        connections.update({word: keys})


def generator(start_words, connections):
    """
    Function, generates sentence with length from 5 to 20.
    """
    try:
        sentence = ''
        length = random.randint(5, 20)
        previous = random.choice(start_words)
        sentence += previous
        for k in range(length):
            sequent = random.choice(connections[previous])
            previous = sequent
            sentence += ' ' + previous
        sentence += '.'
        print(sentence)
        return ''
    except IndexError:
        return ''


def output(n, start_words, connections):
    """
    Function for data output.
    """
    for i in range(n):
        print(generator(start_words, connections))


def main():
    """
    Main Function with all other functions.
    """
    n = control()
    filename = input('Filename: ')
    text, keys, connections, start_words = lists(filename)
    check(text, keys, connections)
    output(n, start_words, connections)


main()
