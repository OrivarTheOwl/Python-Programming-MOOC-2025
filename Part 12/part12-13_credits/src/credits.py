from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts: list):
    total_credits = reduce(lambda credit_sum, course: credit_sum + course.credits, attempts, 0)
    return total_credits

def sum_of_passed_credits(attempts: list):
    filtered = filter(lambda course: course.grade >= 1, attempts)
    final_credits = reduce(lambda credit_sum, course: credit_sum + course.credits, filtered, 0)
    return final_credits

def average(attempts: list):
    filtered = list(filter(lambda course: course.grade >= 1, attempts))
    total_grade = reduce(lambda grade_sum, course: grade_sum + course.grade, filtered, 0)
    return total_grade / len(filtered)

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)