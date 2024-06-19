from model.GenderData import GenderEntry


class GenderModel:
    def __init__(self, data_path):
        self.data_path = data_path

    def get_data_set(self):
        lines = None
        data_buff = []
        output_data_set = {}
        counter = 0

        try:
            with open(self.data_path, encoding="utf8") as dataSet:
                lines = dataSet.readlines()

            if lines and len(lines) > 1:
                # Handle data here
                for line in lines:
                    data = line.split("|")
                    if data[0] == "der" or data[0] == "die" or data[0] == "das":
                        if len(data) == 2:
                            data_entry = GenderEntry(data[0].strip(), data[1].strip())
                            output_data_set.update({counter: data_entry})
                            counter += 1
                        elif len(data) == 3:
                            data_entry = GenderEntry(data[0].strip(), data[1], data[2].strip())
                            output_data_set.update({counter: data_entry})
                            counter += 1
                        word = data_entry.get_word()
                        if word in data_buff:
                            print(word)
                        else:
                            data_buff.append(word)
        except:
            pass

        return output_data_set

    def set_data_set(self, data_set, path):
        with open(path, "r+") as file:
            file.seek(0)
            file.truncate()
            for number in data_set:
                data = data_set[number]
                buff_str = data.get_article() + "|" + data.get_word() + "|" + data.get_translation() + "\n"
                file.write(buff_str)
