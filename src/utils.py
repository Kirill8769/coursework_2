import requests
from random import choice
from config import URL
from basic_word import BasicWord


def load_random_word() -> dict:
    response = requests.get(URL, verify=False)
    random_word = choice(response.json())
    print(random_word)
    basic_word = BasicWord(random_word['word'], random_word['subwords'])
    return basic_word
