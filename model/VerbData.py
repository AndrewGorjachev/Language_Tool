class VerbEntry:
    def __init__(self, verb: str, translation: str, third_person:str, past_tense: str, past_perfect: str, auxiliary_verb: str):
        self.verb = verb
        self.translation = translation
        self.third_person = third_person
        self.past_tense = past_tense
        self.past_perfect = past_perfect
        self.auxiliary_verb = auxiliary_verb

    def get_verb(self):
        return self.verb

    def get_translation(self):
        return self.translation

    def get_past_tense(self):
        return self.past_tense

    def get_past_perfect(self):
        return self.past_perfect

    def get_auxiliary_verb(self):
        return self.auxiliary_verb

    def get_string(self):
        return self.verb + "|" + \
               self.translation + "|" + \
               self.third_person + "|" + \
               self.past_tense + "|" + \
               self.past_perfect + "|" + \
               self.auxiliary_verb