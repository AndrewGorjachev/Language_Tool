class GenderEntry:
    def __init__(self, article: str, word: str, translation: str = ""):
        self.article = article
        self.word = word
        self.translation = translation

    def get_article(self):
        return self.article

    def get_word(self):
        return self.word

    def get_translation(self):
        return self.translation
