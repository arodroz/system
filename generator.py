import random
from googletrans import Translator


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


def make_password(size, adjectives, nouns, language='en'):
    translate = language != 'en'
    if translate:
        translator = Translator()
    random.seed()
    password = ''
    for _ in range(size):
        word = adjectives[get_number(4)]
        if translate:
            word = translator.translate(word, src='en', dest=language)
            word = word.text
        password += word + '_'
        word = nouns[get_number(5)]
        if translate:
            word = translator.translate(word, src='en', dest=language)
            word = word.text
        password += word + '_'
    return password[:-1]


if __name__ == '__main__':

    adjectives = populate('adjectives.csv')
    nouns = populate('nouns.csv')

    password = make_password(2, adjectives, nouns, 'fr')

    print(f"\n{password}\n")
