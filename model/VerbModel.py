from model.CommonModel import CommonModel
from model.VerbData import VerbEntry


class VerbModel(CommonModel):
    def __init__(self, data_path):
        CommonModel.__init__(self, data_path)

    def get_data_set(self):
        lines = self._get_lines()
        output_data_set = {}
        counter = 0

        if lines and len(lines) > 1:
            # Handle data here
            for line in lines:
                data = line.split("|")
                if len(data) == 5:
                    counter += 1
                    auxiliary_verb = data[4].strip().split(" ")[0]
                    past_perfect = data[4].strip().split(" ")[1]
                    data_entry = VerbEntry(verb=data[0].strip(),
                                           translation=data[1].strip(),
                                           third_person=data[2].strip(),
                                           past_tense=data[3].strip(),
                                           auxiliary_verb=auxiliary_verb,
                                           past_perfect=past_perfect)
                    output_data_set.update({counter: data_entry})

        return output_data_set