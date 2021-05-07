# Problem: https://www.hackerrank.com/challenges/time-conversion/problem
# Score: 15.0


def timeConversion(s):
    # Checking if first two elements are 12 and last two elements of time is AM
    if s[:2] == '12' and s[-2:] == 'AM':
        return '00' + s[2:-2]
    # remove the AM      
    elif s[-2:] == 'AM':
        return s[:-2]
    # Checking if first two elements are 12 and last two elements of time is PM
    elif s[:2] == '12' and s[-2:] == 'PM':
        return s[:-2]
    # add 12 to hours and remove PM  
    else:
        return str(int(s[:2]) + 12) + s[2:-2]

s = input()
result = timeConversion(s)
print(result)
