# Problem: https://www.hackerrank.com/challenges/find-a-string/problem
# Score: 10.0


def count_substring(string, sub_string):
    return sum(1 for i in range(len(string)) if string.startswith(sub_string,i))

string = input().strip()
sub_string = input().strip()
result = count_substring(string, sub_string)
print(result)
