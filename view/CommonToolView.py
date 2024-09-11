from view.AskSplashView import AskSplashView
from view.OpenDialogView import OpenDialogView
from view.OpenSplashView import OpenSplashView


class CommonToolView:

    def __init__(self, **kwargs):
        self.total_words=0

    def set_total_answers(self, total_answers):
        self.ids.stat.ids.total_answers.text = str(total_answers)
        answ_percent = 0
        if self.total_words > 0:
            answ_percent = (total_answers / self.total_words * 100)
        self.ids.stat.ids.total_answers_percent.text = format(answ_percent, ".1f") + "%"

    def set_right_answers(self, right_answers):
        self.ids.stat.ids.total_of_right_answers.text = str(right_answers)
        answ_percent = 0
        if self.total_words > 0:
            answ_percent = (right_answers / self.total_words * 100)
        self.ids.stat.ids.total_of_right_answers_percent.text = format(answ_percent, ".1f") + "%"

    def set_wrong_answers(self, wrong_answers: int):
        self.ids.stat.ids.total_of_wrong_answers.text = str(wrong_answers)
        answ_percent=0
        if self.total_words > 0:
            answ_percent=(wrong_answers/self.total_words * 100)
        self.ids.stat.ids.total_of_wrong_answers_percent.text = format(answ_percent, ".1f") + "%"

    def set_total_words(self, total_words):
        self.total_words=total_words
        self.ids.stat.ids.total_of_words.text = str(total_words)

    def on_press_open(self):
        OpenDialogView(self.controller.set_data_path)

    def show_warning(self, warning_message):
        OpenSplashView("Warning", warning_message)

    def show_mistake(self, right_answer):
        OpenSplashView("Mistake", right_answer)

    def show_ask(self, question_message):
        dialog = AskSplashView("", question_message, self.controller.repeat_cb)
        dialog.open()

    def set_data_path(self, file_path):
        self.ids.file_path.text = file_path
