if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_data = input("Course information: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    course_data = "course1.txt"

def grade_calc():
    final_grade = 0
    if 0 <= total_score <= 14:
        final_grade = 0
    elif 15 <= total_score <= 17:
        final_grade = 1
    elif 18 <= total_score <= 20:
        final_grade = 2
    elif 21 <= total_score <= 23:
        final_grade = 3
    elif 24 <= total_score <= 27:
        final_grade = 4
    elif 28 <= total_score:
        final_grade = 5
    return final_grade


students = {}

with open (student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        full_name = parts[1] + " " + parts[2].strip()
        students[parts[0]] = full_name

total_exercise_points = {}
final_exercise_points = {}

with open (exercise_data) as new_file:
    for line in new_file:
        total_exec_points = 0
        parts = line.split(";")
        if parts[0] == "id":
            continue
        for number in parts[1:]:
            total_exec_points += int(number)
        total_exercise_points[parts[0]] = total_exec_points
        completed_points = total_exec_points // 4
        final_exercise_points[parts[0]] = completed_points

exam_points = {}

with open (exam_data) as new_file:
    for line in new_file:
        total_exam_points = 0
        parts = line.split(";")
        if parts[0] == "id":
            continue
        for number in parts[1:]:
            total_exam_points += int(number)
        exam_points[parts[0]] = total_exam_points


open("results.csv", "w").close()
open("results.txt", "w").close()

course_name = ""
course_credits = 0

with open(course_data) as new_file:
    for line in new_file:
        parts = line.split(": ")
        if parts[0] == "name":
            course_name = parts[1].strip()
        elif parts[0] == "study credits":
            course_credits = int(parts[1])

with open("results.txt", "a") as new_file:
    new_file.write(f"{course_name}, {course_credits} credits\n")
    new_file.write("======================================\n")
    new_file.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade'}\n")

for id, name in students.items():
    if id in final_exercise_points:
        if id in exam_points:
            total_score = final_exercise_points[id] + exam_points[id]
            final_grade = grade_calc()

            with open("results.csv", "a") as new_file:
                new_file.write(f"{id};{name};{final_grade}\n")

            with open("results.txt", "a") as new_file:
                new_file.write(f"{name:30}{total_exercise_points[id]:<10}{final_exercise_points[id]:<10}{exam_points[id]:<10}{total_score:<10}{final_grade}\n")