def add_student(student_info: dict, name: str):
    student_info[name] = []



def print_student(student_info: dict, name: str):
    if name in student_info:
        all_pts = 0
        avg_pts = 0
        print(f"{name}:")
        if len(student_info[name]) > 0:
            print(f" {len(student_info[name])} completed courses:")
            for course in range(len(student_info[name])):
                print(f"  {student_info[name][course][0]} {student_info[name][course][1]}")
                all_pts += student_info[name][course][1]
                avg_pts = all_pts / len(student_info[name])
            print(f" average grade {avg_pts}")
        else:
            print(" " + "no completed courses")
    else:
        print(f"{name}: no such person in the database")



def add_course(student_info: dict, name: str, course: tuple):
    unique = True
    if course[1] > 0:
        for each in student_info[name]:
            if course[0] in each[0]:
                if course[1] > each[1]:
                    student_info[name].remove(each)
                    student_info[name].append(course)
                unique = False
        if unique:
            student_info[name].append(course)




def summary(student_info: dict):
    student_count = len(student_info)
    print(f"students {student_count}")

    who_most_courses = ""
    most_courses = 0

    who_best_avg = ""
    best_avg = 0

    for student in student_info:
        courses_completed = len(student_info[student])
        if courses_completed > most_courses:
            most_courses = courses_completed
            who_most_courses = student
    print(f"most courses completed {most_courses} {who_most_courses}")

    for student in student_info:
        all_pts = 0
        avg_pts = 0
        for course in student_info[student]:
            all_pts += course[1]
        avg_pts = all_pts / len(student_info[student])
        if avg_pts > best_avg:
            best_avg = avg_pts
            who_best_avg = student
    print(f"best average grade {best_avg} {who_best_avg}")





if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)