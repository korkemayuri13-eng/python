# Q25. Write a program to keep asking for a number until the user enters zero.
while True:
    n = int(input("enter a number(0 to stop):"))
    if n== 0:
        print ("program stoped.") 
        break 