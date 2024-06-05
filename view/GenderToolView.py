from kivy.uix.screenmanager import Screen

from controller.GenderController import GenderController
from view.AskSplashView import AskSplashView
from view.OpenDialogView import OpenDialogView
from view.OpenSplashView import OpenSplashView
from view.SaveDialogView import SaveDialogView


class GenderToolView(Screen):
    def __init__(self, default_color, **kwargs):
        super(GenderToolView, self).__init__(**kwargs)
        self.controller = GenderController()
        self.controller.set_view(self)
        self.default_color = default_color

    def set_controller(self, controller):
        self.controller = controller
        self.controller.set_view(self)

    def on_press_der(self):
        self.controller.check_answer("der")

    def on_press_die(self):
        self.controller.check_answer("die")

    def on_press_das(self):
        self.controller.check_answer("das")

    def set_word(self, word):
        self.ids.word_to_check.text = word

    def on_press_translate(self):
        translation = self.controller.get_translation()
        if translation:
            OpenSplashView("Translation", translation)

    def on_press_new_word(self):
        article = self.ids.article.text
        word = self.ids.word.text
        translation = self.ids.translation.text

        if article == "der" or \
                article == "die" or \
                article == "das":
            pass
        else:
            OpenSplashView("Warning", "The article field is missing.")
            return
        if not word:
            OpenSplashView("Warning", "The word field is missing.")
            return
        if not translation:
            OpenSplashView("Warning", "The translation field is missing.")
            return
        self.controller.add_new_entry(article, word, translation)

    def set_total_answers(self, total_answers):
        self.ids.total_answers.text = str(total_answers)

    def set_right_answers(self, right_answers):
        self.ids.total_of_right_answers.text = str(right_answers)

    def set_wrong_answers(self, wrong_answers: int):
        self.ids.total_of_wrong_answers.text = str(wrong_answers)

    def set_total_words(self, total_words):
        self.ids.total_of_words.text = str(total_words)

    def set_color(self, name, color):
        col = None
        botton = None
        if color == "red":
            col = (1, 0, 0, 1)
        elif color == "green":
            col = (0, 1, 0, 1)
        else:
            return

        if name == "der":
            botton = self.ids.checkMale
        elif name == "die":
            botton = self.ids.checkFemale
        elif name == "das":
            botton = self.ids.checkNeutral
        else:
            return

        botton.md_bg_color = col

    def reset_colors(self):
        self.ids.checkMale.md_bg_color = self.default_color
        self.ids.checkFemale.md_bg_color = self.default_color
        self.ids.checkNeutral.md_bg_color = self.default_color

    def set_data_path(self, file_path):
        self.ids.file_path.text = file_path

    def get_data_path(self):
        return self.ids.file_path.text

    def on_press_open(self):
        OpenDialogView(self.controller.set_data_path)

    def on_press_default(self):
        OpenDialogView(self.controller.set_data_path, True)

    def on_press_save(self):
        if self.controller.data:
            SaveDialogView(self.controller.save_data, self.controller.new_file)
        else:
            self.show_warning("No data loaded.")

    def show_warning(self, warning_message):
        OpenSplashView("Warning", warning_message)

    def show_mistake(self, right_answer):
        OpenSplashView("Mistake", right_answer)

    def show_ask(self, question_message):
        dialog = AskSplashView("", question_message, self.controller.repeat_cb)
        dialog.open()

    def show_congratulation(self, congratulation_message):
        OpenSplashView("Congratulations", congratulation_message)
