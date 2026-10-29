# Q30. Write a program to search for a number in a list and stop when it is found.

numbers = list(map(int, input("Enter list numbers: ").split()))
search = int(input("Enter number to search: "))

for num in numbers:
    if num == search:
        print("Number found:", num)
        break
else:
    print("Number not found")