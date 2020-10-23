import random


def get_number(length):
    value = ''
    for _ in range(length):
        a = random.randint(1, 6)
        value += str(a)
    return int(value)


def populate(filename):
    with open(filename) as f:
        buf = f.readlines()
    dict = {}
    for line in buf:
        a, b = line.split(',')
        dict[int(a)] = b[:-1]
    return dict


def make_password(size, adjectives, nouns):
    random.seed()
    password = ''
    for _ in range(size):
        password += adjectives[get_number(4)] + '\x20'
        password += nouns[get_number(5)] + '\x20'
    return password[:-1]


if __name__ == '__main__':

    adjectives = populate('adjectives.csv')
    nouns = populate('nouns.csv')

    print(f"\n{make_password(2, adjectives, nouns)}\n")
