def Pattern(n):
    if(n == 0):
        return 
    print('*'* n)
    Pattern(n-1)

n = int(input("Enter your Number to print *:"))   
print(Pattern(n))    

    