from random import choice

import requests

from basic_word import BasicWord


def load_random_word() -> BasicWord:
    """
    Загружает случайное слово с соответствующими подсловами из удаленного ресурса.

    :return: Объект BasicWord, представляющий случайное слово и его подслова.
    """
    response = requests.get("https://jsonkeeper.com/b/O6DZ", verify=False)
    random_word = choice(response.json())
    basic_word = BasicWord(random_word["word"], random_word["subwords"])
    return basic_word
