import requests
from random import choice
from config import URL


def load_random_word():
    response = requests.get(URL, verify=False)
    random_word = choice(response.json())
    return random_word
