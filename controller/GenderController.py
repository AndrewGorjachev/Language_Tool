import os.path
import random
from datetime import datetime

from kivy.clock import Clock

from model.GenderData import DataEntry
from model.GenderModel import GenderModel


class GenderController:
    def __init__(self):
        self.view = None
        self.model = None
        self.data = None
        self.to_repeat = {}
        self.current_step = 0
        self.total_words = 0

    def _reset_statistic(self):
        self.total_words = len(self.data)
        self.current_step = 0
        self.total_answers = 0
        self.right_answers = 0
        self.wrong_answers = 0
        self.random_list = random.sample(range(self.total_words), self.total_words)

    def _check_if_exist(self, word):
        tmp = set()
        for entry in self.data:
            tmp.add(self.data[entry].get_word())
        return word in tmp

    def _init_model(self, data_path):
        self.model = GenderModel(data_path)
        self.data = self.model.get_data_set()
        self._reset_statistic()

    def _update_statistics(self):
        self.view.set_total_answers(self.total_answers)
        self.view.set_right_answers(self.right_answers)
        self.view.set_wrong_answers(self.wrong_answers)
        self.view.set_total_words(self.total_words)

    def _get_random_word(self):
        random_number = self.random_list[self.current_step]
        self.view.set_word(self.data[random_number].get_word())

    def repeat_cb(self, answer: bool):
        if answer:
            self.data = self.to_repeat.copy()
            self.to_repeat.clear()
        else:
            self.to_repeat.clear()
        self._reset_statistic()
        self._update_statistics()
        self._get_random_word()

    def set_view(self, view):
        self.view = view
        if self.model:
            self._get_random_word()
            self._update_statistics()

    def reset_colors_cb(self, dt):
        self.view.reset_colors()

    def check_answer(self, article):
        if self.data:
            print(self.current_step)
            print(self.total_words)

            word_id = self.random_list[self.current_step]
            if article == self.data[word_id].get_article():
                self.right_answers += 1
                self.view.set_color(article, "green")
            else:
                self.wrong_answers += 1
                self.view.set_color(article, "red")
                self.view.set_color(self.data[word_id].get_article(), "green")
                len_to_repeat = len(self.to_repeat)
                self.to_repeat.update({len_to_repeat: self.data[word_id]})
                self.view.show_mistake(self.data[word_id].get_article() +
                                       " " +
                                       self.data[word_id].get_word())
            self.current_step += 1
            self.total_answers += 1
            self._update_statistics()
            Clock.schedule_once(self.reset_colors_cb, 0.75)
            if self.current_step >= self.total_words:
                self.data = self.model.get_data_set()
                self._reset_statistic()
                self._update_statistics()

                if len(self.to_repeat) != 0:
                    self.view.show_ask("Would you like to repeat your mistakes?\n"
                                       "Press \"No\" to repeat all.")
                else:
                    self.view.show_congratulation("You finished the lesson without mistakes!")
            self._get_random_word()
        else:
            self.view.show_warning("Nothing to learn. No data loaded.")

    def set_data_path(self, data_path):
        self.view.set_data_path(data_path)
        self._init_model(data_path)
        if self.data and len(self.data) > 1:
            self._get_random_word()
            self._update_statistics()
        else:
            self.view.show_warning("Nothing to learn.\nNot appropriate data format.")

    def new_file(self, path):
        now = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
        new_path = path + f"/substantive_{now}.txt"
        try:
            if not os.path.exists(new_path):
                open(new_path, "w")
            return new_path
        except:
            self.view.show_warning("Cannot create a new file.")
            return None

    def save_data(self, path):
        try:
            if self.data:
                self.model.set_data_set(self.data, path)
            else:
                self.view.show_warning("No data loaded.")
        except:
            self.view.show_warning("Access file error.")

    def get_translation(self):
        if self.data:
            word_id = self.random_list[self.current_step]
            return self.data[word_id].get_translation()
        else:
            self.view.show_warning("Nothing to learn. No data loaded.")
            return None

    def add_new_entry(self, article, word, translation):
        new_data_entry = DataEntry(article, word, translation)
        if self.data:
            if not self._check_if_exist(word):
                self.data.update({self.total_words: new_data_entry})
                self._reset_statistic()
                self._update_statistics()
            else:
                self.view.show_warning("The entry already exists ")
        else:
            self.view.show_warning("No data loaded.")
