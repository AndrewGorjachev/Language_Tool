from kivy.clock import Clock

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

    def check_answer(self, answer: str):
        if self.data:
            word_id = self.random_list[self.current_step]
            buff = answer.strip()
            self.view.clean_answer()
            if buff.lower() == self.data[word_id].get_word().lower():
                self.right_answers += 1
                self.view.set_color("green")
            else:
                self.wrong_answers += 1
                self.view.set_color("red")
                len_to_repeat = len(self.to_repeat)
                self.to_repeat.update({len_to_repeat: self.data[word_id]})
                self.view.show_mistake(self.data[word_id].get_word() + " - " +
                                       self.data[word_id].get_translation())
            self.current_step += 1
            self.total_answers += 1
            self._update_statistics()
            Clock.schedule_once(self.reset_colors_cb, 0.75)
            if self.current_step >= self.total_words:
                self.data = self.model.get_data_set()
                ask_sentence = self.generate_ask_phrase()
                self._reset_statistic()
                self._update_statistics()
                if len(self.to_repeat) != 0:
                    self.view.show_ask(ask_sentence)
                else:
                    self.view.show_congratulation("You finished the lesson without mistakes!")
            self._get_random_word()
        else:
            self.view.show_warning("Nothing to learn. No data loaded.")
