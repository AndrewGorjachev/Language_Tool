from controller.CommonController import CommonController
from model.VerbModel import VerbModel


class VerbsController(CommonController):

    def __init__(self):
        CommonController.__init__(self)

    def _init_model(self, data_path):
        self.model = VerbModel(data_path)
        self.data = self.model.get_data_set()
        self._reset_statistic()

    def _get_random_word(self):
        random_number = self.random_list[self.current_step]
        self.view.set_translation(self.data[random_number].get_translation())

    def get_translation(self):
        if self.data:
            random_number = self.random_list[self.current_step]
            return self.data[random_number].get_verb()
        else:
            return ""

    def get_auxiliary_verb(self):
        if self.data:
            random_number = self.random_list[self.current_step]
            return self.data[random_number].get_auxiliary_verb()
        else:
            return ""

    def get_perfect_verb(self):
        if self.data:
            random_number = self.random_list[self.current_step]
            return self.data[random_number].get_past_perfect()
        else:
            return ""
