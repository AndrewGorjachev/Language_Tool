from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

from controller.WordsController import WordsController
from view.CommonToolView import CommonToolView
from view.OpenSplashView import OpenSplashView


class WordsToolView(CommonToolView):

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

    def on_yes(self):
        self.controller.check_answer("yes")

    def on_no(self):
        self.controller.check_answer("no")

class WordsToolViewDeutsch(Screen, WordsToolView):
    def __init__(self, default_color, **kwargs):
        super(WordsToolViewDeutsch, self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)
        self.ids.main_title.title = "Die Worten lernen (Deutsch -> Fremdsprache)"
        self.controller = WordsController(False)
        self.controller.set_view(self)
        self.default_color = default_color

class WordsToolViewFremd(Screen, WordsToolView):
    def __init__(self, default_color, **kwargs):
        super(WordsToolViewFremd, self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)
        self.ids.main_title.title = "Die Worten lernen (Fremdsprache -> Deutsch)"
        self.controller = WordsController(True)
        self.controller.set_view(self)
        self.default_color = default_color
