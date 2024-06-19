import random


class CommonController:

    def __init__(self):
        self.view = None
        self.model = None
        self.data = None
        self.to_repeat = {}
        self.current_step = 0
        self.total_words = 0

    def _reset_statistic(self):
        if self.data:
            self.total_words = len(self.data)
            self.current_step = 0
            self.total_answers = 0
            self.right_answers = 0
            self.wrong_answers = 0
            self.random_list = random.sample(range(self.total_words), self.total_words)

    def _update_statistics(self):
        self.view.set_total_answers(self.total_answers)
        self.view.set_right_answers(self.right_answers)
        self.view.set_wrong_answers(self.wrong_answers)
        self.view.set_total_words(self.total_words)

    def set_data_path(self, data_path):
        self.view.set_data_path(data_path)
        self._init_model(data_path)
        if self.data and len(self.data) > 1:
            self.to_repeat = {}
            self._get_random_word()
            self._update_statistics()
        else:
            self.view.show_warning("Nothing to learn.\nNot appropriate data format.")

    def set_view(self, view):
        self.view = view
        if self.model:
            self._get_random_word()
            self._update_statistics()

    def reset_colors_cb(self, dt):
        self.view.reset_colors()

    def repeat_cb(self, answer: bool):
        if answer:
            self.data = self.to_repeat.copy()
            self.to_repeat.clear()
        else:
            self.to_repeat.clear()
        self._reset_statistic()
        self._update_statistics()
        self._get_random_word()

    def generate_ask_phrase(self):
        rate = format(float((self.right_answers / self.total_answers) * 100), ".2f")
        return "Right answers " + str(self.right_answers) + "\n" + \
               "Wrong answers " + str(self.wrong_answers) + "\n" + \
               "Right answers rate " + str(rate) + "% \n" + \
               "Would you like to repeat your mistakes?\n" + \
               "Press \"No\" to repeat all."
