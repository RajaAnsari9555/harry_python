p1="Free money now"
p2="Click here fast"
p3 ="Win cash instantly"
p4 ="Limited offer today"

message  = input("Enter you massage")

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("this message look like spammy")

else:
    print("This message is not spammy")