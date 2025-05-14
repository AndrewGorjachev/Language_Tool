class WordsEntry:
    def __init__(self, word: str, translation: str):
        self.word = word
        self.translation = translation

    def get_word(self):
        return self.word

    def get_translation(self):
        return self.translation
