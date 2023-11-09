import utils
from basic_word import BasicWord
from players import Player


def play_game(basic_word: BasicWord) -> None:
    print("Программа: Ввведите имя игрока")
    user_name = input("Пользователь: ")
    print("---")

    player = Player(user_name, [])

    print(f"Программа: Привет, {player.name}!")
    print(f"Программа: Составьте {basic_word.get_count_subwords()} слов из слова {basic_word.word}")
    print("Программа: Слова должны быть не короче 3 букв")
    print('Программа: Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print("---")
    print("Программа: Поехали, ваше первое слово?")

    while True:
        user_word = input("Пользователь: ")
        if len(user_word) < 3:
            print("Программа: Слишком короткое слово")
        elif user_word.lower() in ["stop", "стоп"]:
            print(f"Программа: Игра завершена. Количество угаданных слов - {player.get_count_used_words()}")
            quit()
        elif not basic_word.get_check_subword(user_word):
            print("Программа: Неверно")
        elif player.get_check_uniq_word(user_word):
            print("Программа: Уже использовано")
        elif basic_word.get_check_subword(user_word):
            print("Программа: Верно")
            player.add_word(user_word)
        print("---")


def main() -> None:
    basic_word = utils.load_random_word()
    play_game(basic_word)


if __name__ == "__main__":
    main()
