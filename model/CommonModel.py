class CommonModel:
    def __init__(self, data_path):
        self.data_path = data_path

    def _get_lines(self):
        lines = None

        try:
            with open(self.data_path, encoding="utf8") as dataSet:
                lines = dataSet.readlines()
        except:
            pass

        return lines