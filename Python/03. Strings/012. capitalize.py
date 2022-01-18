def solve(s):

    for i in s.split():
        s = s.replace(i, i.capitalize())
    
    return s

  
def main():
    
    name = input("Enter a name: ")
    
    result = capitalize(name)

    print(result)

main()
