if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

students = {}

with open (student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        full_name = parts[1] + " " + parts[2].strip()
        students[parts[0]] = full_name

exercises = {}

with open (exercise_data) as new_file:
    for line in new_file:
        total = 0
        parts = line.split(";")
        if parts[0] == "id":
            continue
        for number in parts[1:]:
            total += int(number)
        exercises[parts[0]] = total

for id, name in students.items():
    if id in exercises:
        total_score = exercises[id]
    print(f"{name} {total_score}")