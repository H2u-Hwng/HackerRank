# Problem: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Score: 20.0


from collections import namedtuple
n = int(input()) 
columns = input().split()
total = 0
for _ in range(n):
    students = namedtuple('student', columns)
    column1, column2, column3, column4 = input().split()
    student = students(column1, column2, column3, column4)
    total += int(student.MARKS)
average = total/n
print('%.2f' % average)
