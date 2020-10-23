import random


def get_number(length):
    value = ''
    for i in range(length):
        a = random.randint(1, 6)
        value += str(a)
    return int(value)


if __name__ == '__main__':

    adjectives = {}
    with open('adjectives.csv') as f:
        buf = f.readlines()
    for line in buf:
        a, b = line.split(',')
        adjectives[int(a)] = b[:-1]

    nouns = {}
    with open('nouns.csv') as f:
        buf = f.readlines()
    for line in buf:
        a, b = line.split(',')
        nouns[int(a)] = b[:-1]

    random.seed()

    word_1 = adjectives[get_number(4)]
    word_2 = nouns[get_number(5)]
    word_3 = adjectives[get_number(4)]
    word_4 = nouns[get_number(5)]

    print(f"\n{word_1} {word_2} {word_3} {word_4}\n")
