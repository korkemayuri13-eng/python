# Q18. Write a program to print the multiplication table of a given number.
num = int (input("enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
    