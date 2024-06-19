import os.path
import random
from datetime import datetime

from kivy.clock import Clock

from controller.CommonController import CommonController
from model.GenderData import GenderEntry
from model.GenderModel import GenderModel


class GenderController(CommonController):
    def __init__(self):
        CommonController.__init__(self)

    def _check_if_exist(self, word):
        tmp = set()
        for entry in self.data:
            tmp.add(self.data[entry].get_word())
        return word in tmp

    def _init_model(self, data_path):
        self.model = GenderModel(data_path)
        self.data = self.model.get_data_set()
        self._reset_statistic()

    def _get_random_word(self):
        random_number = self.random_list[self.current_step]
        self.view.set_word(self.data[random_number].get_word())

    def check_answer(self, article):
        if self.data:
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
                                       self.data[word_id].get_word() + " - " +
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
        new_data_entry = GenderEntry(article, word, translation)
        if self.data:
            if not self._check_if_exist(word):
                self.data.update({self.total_words: new_data_entry})
                self._reset_statistic()
                self._update_statistics()
            else:
                self.view.show_warning("The entry already exists ")
        else:
            self.view.show_warning("No data loaded.")
