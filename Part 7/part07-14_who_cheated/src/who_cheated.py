import csv
from datetime import datetime, timedelta



def cheaters():
    cheater_list = []
    student_list = {}

    with open("start_times.csv") as new_file:
        for line in csv.reader(new_file, delimiter=";"):
            start_time = datetime.strptime(line[1], "%H:%M")
            student_list[line[0]] = {"start": start_time, "end": None}

    with open("submissions.csv") as new_file:
        for line in csv.reader(new_file, delimiter=";"):
            if line[0] in student_list:
                end_time = datetime.strptime(line[3], "%H:%M")
                student_list[line[0]]["end"] = end_time

                time_diff = student_list[line[0]]["end"] - student_list[line[0]]["start"]
                if time_diff.seconds > 3600*3 and line[0] not in cheater_list:
                    cheater_list.append(line[0])

    return cheater_list
