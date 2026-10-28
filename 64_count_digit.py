# Q22. Write a program to count the digits in a number.
n = int(input("enter a number:"))
n = abs (n)
count = 0
if n == 0:
    count = 1
else :
    while n> 0:
        count += 1
        n //= 10
        print ("number of digits =",count)
        