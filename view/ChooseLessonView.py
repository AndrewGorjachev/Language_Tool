from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("view/ChooseLessonView.kv")


class ChooseLessonView(Screen):
    def __init__(self, **kwargs):
        super(ChooseLessonView, self).__init__(**kwargs)
