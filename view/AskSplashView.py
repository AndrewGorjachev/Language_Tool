from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


class AskSplashView(MDDialog):

    def __init__(self, title, message, call_back):
        super().__init__(title=title,
                         text=message,
                         auto_dismiss='False',
                         buttons=[
                             MDFlatButton(text="Ja",
                                          on_release=self.on_pressed_yes),
                             MDFlatButton(text="Nein",
                                          on_release=self.on_pressed_no)
                            ]
                         )
        self.repeat_mistakes = call_back
        super().open()

    def on_pressed_yes(self, object):
        self.repeat_mistakes(True)
        self.dismiss()

    def on_pressed_no(self, object):
        self.repeat_mistakes(False)
        self.dismiss()
