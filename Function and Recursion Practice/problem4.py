def Sum(n):
    if(n ==1 ):
        return 1
    return Sum(n-1)+n

n = int(input("Enter your number:"))
print(Sum(n))