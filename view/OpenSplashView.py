from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


class OpenSplashView():

    def __init__(self, title, message):
        self.dialog = MDDialog(
            title=title,
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda _: self.dialog.dismiss()
                )
            ]
        )
        self.dialog.open()
