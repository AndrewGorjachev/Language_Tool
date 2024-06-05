import os

from kivy.utils import platform
from kivymd.uix.filemanager import MDFileManager

from view.OpenSplashView import OpenSplashView


class OpenDialogView:

    def __init__(self, call_back, use_root=False):
        self.file_manager = MDFileManager(
            select_path=self.on_pressed_load,
            exit_manager=self.on_pressed_cancel
        )
        self.call_back = call_back
        self.path = ''
        if platform == 'win32':
            self.path = str(os.getcwd()).replace('\\', '\\\\')
        if platform == 'linux' or platform == 'macosx':
            self.path = str(os.getcwd())
        elif platform == 'android' and not use_root:
            self.path = '/storage/emulated/0/'
        else:
            self.path = str(os.getcwd())
        self.file_manager.show(self.path)

    def on_pressed_cancel(self, optional):
        self.file_manager.close()

    def on_pressed_load(self, path):
        self.file_manager.close()

        if len(path) != 0:
            self.call_back(path)
        else:
            OpenSplashView("Warning", "Source data is not chosen.")
