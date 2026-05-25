def main():

 try:
    a = int(input("Enter your Number"))
    print(a)
    return
 except Exception as e:
    print(e)
    return
 finally:
    print("hey i am inside Finally") 
 print("hello from MD Raja")    
main();