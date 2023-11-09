class Player:
    def __init__(self, name: str, subwords: list[str]):
        self.name = name
        self.subwords = subwords

    def __repr__(self) -> str:
        return f"name: {self.name}\nused_subwords: {self.subwords}"

    def get_count_used_words(self) -> int:
        """
        Подсчитывает количество использованных слов

        :return: Количество использованных слов
        """
        return len(self.subwords)

    def add_word(self, word: str) -> None:
        """
        Добавляет слово в список использованных слов

        :param word: Использованное слово
        """
        if not self.get_check_uniq_word(word):
            self.subwords.append(word)

    def get_check_uniq_word(self, word: str) -> bool:
        """
        Проверяет было ли использовано данное слово до этого

        :param word: Слово для проверки

        :return: Результат проверки
        """
        return word in self.subwords
