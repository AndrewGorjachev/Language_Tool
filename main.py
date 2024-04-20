from kivy.app import App

from view.gende_tool_view import GenderToolView

class LanguageTool(App):
    def build(self):
        return GenderToolView()

if __name__ == '__main__':
    LanguageTool().run()
