import csv
from datetime import datetime, timedelta

def final_points():
    student_list = {}
    final_points_dict = {}

    with open("start_times.csv") as new_file:
        for line in csv.reader(new_file, delimiter=";"):
            start_time = datetime.strptime(line[1], "%H:%M")
            student_list[line[0]] = {"start": start_time, "end": None, "tasks": {}}

    with open("submissions.csv") as new_file:
        for line in csv.reader(new_file, delimiter=";"):
            if line[0] in student_list:
                end_time = datetime.strptime(line[3], "%H:%M")
                task_num = int(line[1])
                point_value = int(line[2])
                student_list[line[0]]["end"] = end_time

                time_diff = student_list[line[0]]["end"] - student_list[line[0]]["start"]
                if time_diff < timedelta(hours=3):
                    if task_num not in student_list[line[0]]["tasks"] or point_value > student_list[line[0]]["tasks"][task_num]:
                        student_list[line[0]]["tasks"][task_num] = point_value

    for student in student_list:
        point_sum = sum(student_list[student]["tasks"].values())
        final_points_dict[student] = point_sum

    return final_points_dict