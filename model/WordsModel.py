from model.CommonModel import CommonModel
from model.WordsData import WordsEntry


class WordsModel(CommonModel):
    def __init__(self, data_path):
        CommonModel.__init__(self, data_path)

    def get_data_set(self):
        lines = self._get_lines()
        data_buff = []
        output_data_set = {}
        counter = 0

        if lines and len(lines) > 1:
            # Handle data here
            for line in lines:
                data = line.split("|")
                if data:
                    data_entry = None
                    if len(data) == 2:
                        data_entry = WordsEntry(data[0].strip(), data[1].strip())
                        output_data_set.update({counter: data_entry})
                        counter += 1
                    if len(data) == 3:
                        data_entry = WordsEntry(data[1].strip(), data[2].strip())
                        output_data_set.update({counter: data_entry})
                        counter += 1
                    if data_entry:
                        word = data_entry.get_word()
                        if word in data_buff:
                            print(word)
                        else:
                            data_buff.append(word)
        return output_data_set

    def set_data_set(self, data_set, path):
        with open(path, "r+") as file:
            file.seek(0)
            file.truncate()
            for number in data_set:
                data = data_set[number]
                buff_str = data.get_word() + "|" + data.get_translation() + "\n"
                file.write(buff_str)