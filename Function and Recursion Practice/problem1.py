def greatest(a , b ,c):
    if(a>b and a>c ):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = int(input("Enter Your First Number :"))    
b = int(input("Enter Your Second Number :"))
c = int(input("Enter your Third Number :3"))

print(greatest(a , b ,c))