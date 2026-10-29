# Q27. Write a program to skip multiples of 3 using continue.

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i)
