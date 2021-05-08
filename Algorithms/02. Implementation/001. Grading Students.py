# Problem: https://www.hackerrank.com/challenges/grading/problem
# Score: 10.0


def gradingStudents(grade):
    if grade >= 38:
        if grade % 5 >2:
            grade += 5 - (grade % 5)
    return grade

grades_count = int(input().strip())

for _ in range(grades_count):
    grade = int(input().strip())
    result = gradingStudents(grade)
    print(result)
