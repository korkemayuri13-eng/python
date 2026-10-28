# Q19. Write a program to calculate the sum of the first n natural numbers.
n = int (input("enter a positive number :"))
total = 0
for i in range (1,n+ 1):
    total = total + i
    print ("sum=", total)
