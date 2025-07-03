if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

students = {}

with open (student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        full_name = parts[1] + " " + parts[2].strip()
        students[parts[0]] = full_name

exercise_points = {}

with open (exercise_data) as new_file:
    for line in new_file:
        total_exercise_points = 0
        parts = line.split(";")
        if parts[0] == "id":
            continue
        for number in parts[1:]:
            total_exercise_points += int(number)
        completed_points = total_exercise_points // 4
        exercise_points[parts[0]] = completed_points

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



for id, name in students.items():
    if id in exercise_points:
        if id in exam_points:
            total_score = exercise_points[id] + exam_points[id]

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

    print(f"{name} {final_grade}")