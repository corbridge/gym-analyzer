import re
import unidecode

class GymAnalyzer:
    def __init__(self) -> None:
        self.main_regex = r"(?P<date>[0-9]+/[0-9]+/[0-9]+), (?P<hour>[0-9]+:[0-9]+ [A-Za-z]\. [A-Za-z]\.) - [A-Za-z0-9]+: (?P<exercise>[A-Za-z]+( |[A-Za-z]+)+)"
        self.exercise_regex = r"(?P<weight>[0-9]+\s[A-Za-z0-9]+) - (?P<reps>[0-9]+)"
        pass

    def _read_txt(self):
        day_data = ('date', 'hour', 'exercise')
        day_data_list = []
        with open("gym-notes-18-feb.txt","r", encoding="utf8")as file:
            lines = file.readlines()
            for line in lines:
                if re.search(self.main_regex, line):
                    try:
                        parsed_day_exercise = list(re.search(self.main_regex, line).groups())
                    except AttributeError:
                        parsed_day_exercise = list(re.search(self.main_regex, line))        
                    day_data_dict = dict(zip(day_data, parsed_day_exercise))
                    day_data_list.append(day_data_dict)
        return day_data_list

analyzer = GymAnalyzer()
day_data = analyzer._read_txt()
print(day_data)