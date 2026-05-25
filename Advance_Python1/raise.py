a = int(input("Enter your first number"))
b = int(input("Enter your Second number"))

if(b ==0):
    raise ZeroDivisionError("hey our progrma not mean devide by zero")

else:
 print(f"the division a and b is {a /b}")