English = int(input("Enter your marks 1:"))

Hindi= int(input("Enter your marks 2:"))

Math = int(input("Enter your marks 3:"))

total_percentage = ((English+Hindi+Math)*100)/300

if(total_percentage >= 40 and English>=33 and Math >=33 and Hindi>=33):
    print("you are passed" , total_percentage)

else:
    print("You are failed try again" , total_percentage)


