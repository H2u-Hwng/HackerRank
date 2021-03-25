# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score: 10.0


from statistics import mean
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
query_scores = student_marks[query_name]
result = mean(query_scores)
print('{0:.2f}'.format(result))
