from kivy.uix.screenmanager import Screen

from controller.GenderController import GenderController
from view.AskSplashView import AskSplashView
from view.CommonToolView import CommonToolView
from view.OpenDialogView import OpenDialogView
from view.OpenSplashView import OpenSplashView
from view.SaveDialogView import SaveDialogView


class GenderToolView(Screen, CommonToolView):
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

    def get_data_path(self):
        return self.ids.file_path.text

    def on_press_default(self):
        OpenDialogView(self.controller.set_data_path, True)

    def on_press_save(self):
        if self.controller.data:
            SaveDialogView(self.controller.save_data, self.controller.new_file)
        else:
            self.show_warning("No data loaded.")

    def on_press_save_mistakes(self):
        if self.controller.to_repeat and len(self.controller.to_repeat) > 0:
            SaveDialogView(self.controller.save_mistakes, self.controller.new_file)
        else:
            self.show_warning("There are no mistakes to save.")

    def show_congratulation(self, congratulation_message):
        OpenSplashView("Congratulations", congratulation_message)
