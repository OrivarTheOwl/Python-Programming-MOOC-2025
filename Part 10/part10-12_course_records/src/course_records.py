class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.name = name
        self.grade = grade
        self.credits = credits
    
    def get_name(self):
        return self.name
    
    def get_grade(self):
        return self.grade
    
    def get_credits(self):
        return self.credits


class CourseList:
    def __init__(self):
        self.course_list = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.course_list:
            course = Course(name, grade, credits)
            self.course_list[course.get_name()] = course
        else:
            if self.course_list[name].grade < grade:
                self.course_list[name].grade = grade

    def print_data(self, name: str):
        course_name = name
        if course_name not in self.course_list:
            print("no entry for this course")
        else:
            course_obj = self.course_list[name]
            print(f"{course_obj.get_name()} ({course_obj.get_credits()} cr) grade {course_obj.get_grade()}")

    def statistics(self):
        credit_total = 0
        grade_total = 0
        grade_iterator = 5
        all_grades = [0, 0, 0, 0, 0]
        for obj_data in self.course_list.values():
            credit_total += obj_data.credits
            grade_total += obj_data.grade
            all_grades[obj_data.grade - 1] += 1

        print(f"{len(self.course_list)} completed courses, a total of {credit_total} credits")
        print(f"mean {grade_total / len(self.course_list):.1f}")
        print("grade distribution")
        while grade_iterator > 0:
            print(f"{grade_iterator}: {(all_grades[grade_iterator - 1]) * 'x'}")
            grade_iterator -= 1


class UserInterface:
    def __init__(self):
        self.data = CourseList()

    def instructions(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def run(self):
        self.instructions()
        while True:
            print("")
            user_input = input("command: ")

            if user_input == "1":
                self.add_course()
            elif user_input == "2":
                self.print_data()
            elif user_input == "3":
                self.statistics()
            elif user_input == "0":
                break

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.data.add_course(name, grade, credits)

    def print_data(self):
        name = input("course: ")
        self.data.print_data(name)

    def statistics(self):
        self.data.statistics()

test = UserInterface()
test.run()