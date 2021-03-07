# Problem: https://www.hackerrank.com/challenges/python-mutations/problem
# Score: 10.0


def mutate_string(string, position, character):
    return '{}{}{}'.format(string[:position], character, string[position + 1:])
    

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
