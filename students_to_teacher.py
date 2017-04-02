# created three dictionarie nd add keys to it
# add key values to dictionaries

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


# Add your function below!
# define a function average to get the average of numbers
def average(numbers):
    total = sum(numbers)  # sum of total numbers
    total = float(total)
    return total / len(numbers)


# define a function to get average of keys by give values

def get_average(student):
    homework = average(student["homework"]) * 0.10
    quizzes = average(student["quizzes"]) * 0.30
    tests = average(student["tests"]) * 0.60
    return homework + quizzes + tests


students = [lloyd, alice, tyler]  # list of students


# define the conditions for grades
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"


def get_class_average(students):
    results = []
    for student in students:  # loop for students in dictionaries
        result = get_average(student)
        results.append(result)  # append the reult
    return average(results)
    # print the function to get result


print get_class_average(students)
print get_letter_grade(get_class_average(students))

