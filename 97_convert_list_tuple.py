# 97. Write a Python program to convert a list into a tuple and a tuple into a list.

my_list = [10, 20, 30, 40, 50]

my_tuple = tuple(my_list)

print("List to Tuple:", my_tuple)

new_list = list(my_tuple)

print("Tuple to List:", new_list)
