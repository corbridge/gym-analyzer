import re
import unidecode
import pandas as pd
import calmap
import matplotlib.pyplot as plt
from datetime import datetime

class GymAnalyzer:
    def __init__(self) -> None:
        self.main_regex = r"(?P<date>[0-9]+/[0-9]+/[0-9]+), (?P<hour>[0-9]+:[0-9]+ [A-Za-z]\. [A-Za-z]\.) - [A-Za-z0-9]+: (?P<exercise>[A-Za-z]+( |[A-Za-z]+)+)"
        self.exercise_regex = r"(?P<weight>[0-9]+\s[A-Za-z0-9]+) - (?P<reps>[0-9]+)"

    def _read_txt(self):
        day_data = ('date', 'hour', 'exercise')
        day_data_list = []
        with open("gym-notes-1-mar.txt","r", encoding="utf8")as file:
            lines = file.readlines()
            for line in lines:
                if re.search(self.main_regex, line):
                    try:
                        parsed_day_exercise = list(re.search(self.main_regex, line).groups())
                    except AttributeError:
                        parsed_day_exercise = list(re.search(self.main_regex, line))        
                    day_data_dict = dict(zip(day_data, parsed_day_exercise))
                    day_data_list.append(day_data_dict)
        self._convert_date_format(day_data_list)
        return day_data_list
    
    def _convert_date_format(self, list_dict_dates):
        for item in list_dict_dates:
            date = datetime.strptime(item["date"], "%d/%m/%Y")
            item["date"] = date.strftime('%Y-%m-%d')
    
    def plot_calendar(self, data):
        df = pd.DataFrame(data)
        df['Datetime'] = pd.to_datetime(df['date'], format='mixed')
        events = pd.Series(0.1, index=df['Datetime'])

        calmap.calendarplot( events)
        plt.show()


analyzer = GymAnalyzer()
day_data = analyzer._read_txt()
analyzer.plot_calendar(day_data)