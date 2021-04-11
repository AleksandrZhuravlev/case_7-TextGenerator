# Case 7
# Programmers:
# Alexander Zhuravlev (75%)

import random

text = []
keys = []
connections = {}
start_words = []
with open('input.txt', 'r', encoding='UTF-8') as inp:
    for stroka in inp:
        for word in stroka.split():
            text.append(word)
            if word[0].isupper() == True:
                start_words.append(word)

for i in text:
    for j in range(len(text)):
        if text[j] == i:
            try:
                keys.append(text[j + 1])
            except:
                pass
    connections.update({i: keys})
    keys = []


def sentence():
    '''
    function generates sentence
    with lenght from 5 to 20
    '''
    sent = ''
    length = random.randint(5, 20)
    prev = random.choice(start_words)
    sent += prev
    for i in range(length):
        next = random.choice(connections[prev])
        prev = next
        sent += ' ' + prev
    sent += '.'
    print(sent)
    return ''


for i in range(10):
    print(sentence())
