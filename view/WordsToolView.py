from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty

from controller.WordsController import WordsController
from view.AskSplashView import AskSplashView
from view.OpenDialogView import OpenDialogView
from view.OpenSplashView import OpenSplashView


class WordsToolView(Screen):

    def __init__(self, default_color, **kwargs):
        super(WordsToolView, self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)
        self.controller = WordsController()
        self.controller.set_view(self)
        self.default_color = default_color
        self.ids.answer_to_check.focus = True

    def on_press_check(self):
        self.controller.check_answer(self.ids.answer_to_check.text)

    def on_press_open(self):
        OpenDialogView(self.controller.set_data_path)

    def set_data_path(self, file_path):
        self.ids.file_path.text = file_path

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:  # 40 - Enter key pressed
            self.controller.check_answer(self.ids.answer_to_check.text)

    def set_word(self, word: str):
        self.ids.word_to_check.text = word

    def set_total_answers(self, total_answers: int):
        self.ids.total_answers.text = str(total_answers)

    def set_right_answers(self, right_answers: int):
        self.ids.total_of_right_answers.text = str(right_answers)

    def set_wrong_answers(self, wrong_answers: int):
        self.ids.total_of_wrong_answers.text = str(wrong_answers)

    def set_total_words(self, total_words: int):
        self.ids.total_of_words.text = str(total_words)

    def set_color(self, color: str):
        col = None
        if color == "red":
            col = (1, 0, 0, 1)
        elif color == "green":
            col = (0, 1, 0, 1)
        else:
            return
        self.ids.check_answer.md_bg_color = col
        self.ids.answer_to_check.focus = True

    def reset_colors(self):
        self.ids.check_answer.md_bg_color = self.default_color

    def clean_answer(self):
        self.ids.answer_to_check.text = str(" ")

    def show_warning(self, warning_message):
        OpenSplashView("Warning", warning_message)

    def show_mistake(self, right_answer):
        OpenSplashView("Mistake", right_answer)

    def show_ask(self, question_message):
        dialog = AskSplashView("", question_message, self.controller.repeat_cb)
        dialog.open()
