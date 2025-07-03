# Collects user inputs, splits them, and stores them in
# exam_points and exercise_points fields and then returns those
def points():
    exam_points = []
    exercise_points = []
    while True:
        large_input = input("Exam points and exercises completed:")
        if large_input == "":
            print("Statistics:")
            break
        else:
            points = large_input.split()
            exam_points.append(points[0])
            exercise_points.append(points[1])
    exam_points = list(map(int, exam_points))
    exercise_points = list(map(int, exercise_points))
    return exam_points, exercise_points


# Combines the scores based off of the method of adding 1 point to the
# exam_points for every 10 exercise_points, rounded down
#
# Also provides a list of the grade counts for each rating 0-5, and returns
# both the combined_score list and grade_count list
def grade_scale(exam_points : int, exercise_points : int):
    grade_count = [0, 0, 0, 0, 0, 0]
    combined_score = []
    i = 0
    while i < len(exam_points):
        combined_score.append(exam_points[i] + int((exercise_points[i] / 10)))
        if  exam_points[i] < 10 or combined_score[i] <= 14:
            grade_count[0] += 1
        elif 15 <= combined_score[i] <= 17:
            grade_count[1] += 1
        elif 18 <= combined_score[i] <= 20:
            grade_count[2] += 1
        elif 21 <= combined_score[i] <= 23:
            grade_count[3] += 1
        elif 24 <= combined_score[i] <= 27:
            grade_count[4] += 1
        elif 28 <= combined_score[i] <= 30:
            grade_count[5] += 1
        i += 1
    return combined_score, grade_count


# Various calculations for the average points between all entries in the
# combined_score list, and also averages the pass percentage based on the
# amount entries above entry 0 in the grade_count list
#
# Prints out the points average and pass percentage, as well as a * for
# every grade entry in each grade_count field
def calculations(combined_score, grade_count):
    average_points = round(sum(combined_score) / len(combined_score), 1)
    print(f"Points average: {average_points}")

    pass_percentage = round((sum(grade_count[1:]) / len(combined_score)) * 100, 1)
    print(f"Pass percentage: {pass_percentage}")

    print("Grade distribution: ")

    i = 5

    while i >= 0:
        print(f"{i}: " + "*" * grade_count[i])
        i -= 1


def main():
    exam_points, exercise_points = points()
    combined_score, grade_count = grade_scale(exam_points, exercise_points)
    calculations(combined_score, grade_count)


main()