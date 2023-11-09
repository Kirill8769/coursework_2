class BasicWord:
    def __init__(self, word: str, subwords: list[str]):
        self.word = word
        self.subwords = subwords

    def __repr__(self) -> str:
        return f"question word: {self.word}\nsubwords: {self.subwords}"

    def get_check_subword(self, subword: str) -> bool:
        """
        Проверяет наличие введенного слова в списке допустимых подслов

        :param subword: Подслово

        :return: Результат проверки
        """
        return subword in self.subwords

    def get_count_subwords(self) -> int:
        """
        Считает количество подслов

        :return: Количество подслов
        """
        return len(self.subwords)
