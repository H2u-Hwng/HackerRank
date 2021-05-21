# Problem: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Score: 30.0


n = int(input())

phoneBook= {}
for _ in range(n):
    multiple_input = input().strip().split()
    phoneBook[multiple_input[0]] = multiple_input[1]
    
while True:
    try:
        name = input()
        if name in phoneBook:
            print(name, '=', phoneBook[name], sep='')
        else:
            print('Not found')
    except:
        break
