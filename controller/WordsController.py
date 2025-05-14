from controller.CommonController import CommonController
from model.WordsModel import WordsModel


class WordsController(CommonController):

    def __init__(self):
        CommonController.__init__(self)

    def _init_model(self, data_path):
        self.model = WordsModel(data_path)
        self.data = self.model.get_data_set()
        self._reset_statistic()

    def _get_random_word(self):
        random_number = self.random_list[self.current_step]
        self.view.set_word(self.data[random_number].get_translation())
