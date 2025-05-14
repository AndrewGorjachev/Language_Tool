from gettext import translation

from kivy.uix.screenmanager import Screen
from controller.VerbsController import VerbsController
from view.CommonToolView import CommonToolView


class VerbsToolView(Screen, CommonToolView):
    def __init__(self, default_color, **kwargs):
        super(VerbsToolView, self).__init__(**kwargs)
        self.controller = VerbsController()
        self.controller.set_view(self)
        self.default_color = default_color

    def on_show_perfect_verb(self):
        perfect = self.controller.get_perfect_verb()
        if perfect:
            self.ids.perfect_verb.text = perfect
        else:
            self.show_warning("Nichts zu lernen. Keine Daten geladen.")

    def on_show_auxiliary_verb(self):
        auxiliary_verb = self.controller.get_auxiliary_verb()
        if auxiliary_verb:
            self.ids.auxiliary_verb.text = auxiliary_verb
        else:
            self.show_warning("Nichts zu lernen. Keine Daten geladen.")

    def on_yes(self):
        self.controller.check_answer("yes")

    def on_no(self):
        self.controller.check_answer("no")

    def set_translation(self, translation):
        self.ids.translation.text = translation
        self.ids.auxiliary_verb.text = ""
        self.ids.perfect_verb.text = ""