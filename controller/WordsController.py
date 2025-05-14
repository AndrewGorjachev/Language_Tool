from controller.CommonController import CommonController
from model.WordsModel import WordsModel


class WordsController(CommonController):

    def __init__(self,direction):
        CommonController.__init__(self)
        self.direction=direction

    def _init_model(self, data_path):
        self.model = WordsModel(data_path)
        self.data = self.model.get_data_set()
        self._reset_statistic()

    def _get_random_word(self):
        random_number = self.random_list[self.current_step]
        if self.direction:
            self.view.set_word(self.data[random_number].get_translation())
        else:
            self.view.set_word(self.data[random_number].get_word())

    def get_translation(self):
        if self.data:
            random_number = self.random_list[self.current_step]
            if self.direction:
                return self.data[random_number].get_word()
            else:
                return self.data[random_number].get_translation()
        else:
            return ""

    def get_word(self):
        if self.data:
            random_number = self.random_list[self.current_step]
            if self.direction:
                return self.data[random_number].get_translation()
            else:
                return self.data[random_number].get_word()
        else:
            return ""