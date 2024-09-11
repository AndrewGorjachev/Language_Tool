from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

from controller.WordsController import WordsController
from view.CommonToolView import CommonToolView
from view.OpenDialogView import OpenDialogView


class WordsToolView(Screen, CommonToolView):

    def __init__(self, default_color, **kwargs):
        super(WordsToolView, self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)
        self.controller = WordsController()
        self.controller.set_view(self)
        self.default_color = default_color
        self.ids.answer_to_check.focus = True

    def on_press_check(self):
        self.controller.check_answer(self.ids.answer_to_check.text)

    def set_data_path(self, file_path):
        self.ids.file_path.text = file_path

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:  # 40 - Enter key pressed
            self.controller.check_answer(self.ids.answer_to_check.text)

    def set_word(self, word: str):
        self.ids.word_to_check.text = word

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
