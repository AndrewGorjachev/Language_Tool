import os

from kivy.utils import platform
from kivymd.uix.filemanager import MDFileManager

from view.OpenSplashView import OpenSplashView


class SaveDialogView:

    def __init__(self, call_back_save, call_back_new, **kwargs):
        self.file_manager = MDFileManager(
            icon_selection_button="plus",
            select_path=self.on_pressed_save,
            exit_manager=self.on_pressed_cancel
        )
        self.call_back_save = call_back_save
        self.call_back_new = call_back_new
        self.path = ""
        if platform == 'win32':
            self.path = str(os.getcwd()).replace('\\', '\\\\')
        elif platform == 'linux' or platform == 'macosx':
            self.path = str(os.getcwd())
        elif platform == "android":
            self.path = "/storage/emulated/0/"
        else:
            self.path = "/"
        self.file_manager.show(self.path)

    def on_pressed_cancel(self, optional):
        self.file_manager.close()

    def on_pressed_save(self, path):
        self.file_manager.close()

        full_path = self.call_back_new(path)

        if full_path:
            self.call_back_save(full_path)
        else:
            OpenSplashView("Warnung", "Die Quelldaten werden nicht ausgewählt.")
