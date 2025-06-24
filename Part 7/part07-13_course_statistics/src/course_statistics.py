import urllib.request
import json

def retrieve_all():
    course_list = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    courses = json.loads(data)

    for course in courses:
        if course["enabled"] == True:
            course_name = course["fullName"]
            short_name = course["name"]
            year = course["year"]
            exercises = sum(course["exercises"])

            course_info = (course_name, short_name, year, exercises)
            course_list.append(course_info)

    return course_list


def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_request.read()
    course = json.loads(data)

    hours = 0
    exercises = 0
    student_count = 0

    for key, value in course.items():
        if value["students"] > student_count:
            student_count = value["students"]
        hours += value["hour_total"]
        exercises += value["exercise_total"]

    avg_hours = int(hours / student_count)
    average_exercises = int(exercises / student_count)
    
    course_info = {}
    course_info["weeks"] = len(course)
    course_info["students"] = student_count
    course_info["hours"] = hours
    course_info["hours_average"] = avg_hours
    course_info["exercises"] = exercises
    course_info["exercises_average"] = average_exercises

    return course_info


if __name__ == "__main__":
    retrieve_all()
    retrieve_course("docker2019")