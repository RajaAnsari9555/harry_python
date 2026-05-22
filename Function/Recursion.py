def Factorial(n):
 if n == 0 or n==1:
    return 1
 return n * Factorial(n-1)

n = int(input("Enter Your Number:"))

print(f"The Factorial of {Factorial(n)}")