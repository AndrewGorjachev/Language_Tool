from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.utils import platform
from kivymd.app import MDApp

from view.ChooseLessonView import ChooseLessonView
from view.GenderToolView import GenderToolView
from view.PronounsToolView import PronounsToolView
from view.VerbsToolView import VerbsToolView
from view.WordsToolView import WordsToolView


class LanguageTool(MDApp):

    def __init__(self, **kwargs):
        super(LanguageTool, self).__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.sm = ScreenManager(transition=FadeTransition())
        self.sm.add_widget(ChooseLessonView(name="ChooseLessonView"))
        self.sm.add_widget(GenderToolView(self.theme_cls.primary_color, name="GenderToolView"))
        self.sm.add_widget(PronounsToolView(self.theme_cls.primary_color, name="PronounsToolView"))
        self.sm.add_widget(VerbsToolView(self.theme_cls.primary_color, name="VerbsToolView"))
        self.sm.add_widget(WordsToolView(self.theme_cls.primary_color, name="WordsToolView"))

        return self.sm

    def change_screen(self, screen_name):
        print("change_screen")
        print(screen_name)
        self.sm.current = screen_name


if __name__ == '__main__':
    if platform == "android":
        from android.permissions import request_permissions, Permission

        request_permissions(
            [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.MANAGE_EXTERNAL_STORAGE])

    lt = LanguageTool()
    lt.run()
