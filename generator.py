import random
from googletrans import Translator


def get_number(size):
    number = ''
    for _ in range(size):
        digit = random.randint(1, 6)
        number += str(digit)
    return int(number)


def populate(filename):
    with open(filename) as f:
        buf = f.readlines()
    dict = {}
    for line in buf:
        key, word = line.split(',')
        dict[int(key)] = word[:-1]
    return dict


def make_password(size, adjectives, nouns, language='en'):
    """Generate password

    Args:
        size (int): Number of adjective/noun pairs
        adjectives (dictionary): English adjectives table
        nouns (dictionary): English nouns table
        language (str, optional): Language in which to translate the words. Defaults to 'en'.

    Returns:
        string: Generated password
    """
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
