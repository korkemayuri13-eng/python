# Q23. Write a program to find the sum of the digits of a number.
n = abs(int(input("enter a number:")))
total = 0 
while n > 0:
    digit = n % 10
    total += digit 
    n //=10
    print ("sum of digit =",total) 
    