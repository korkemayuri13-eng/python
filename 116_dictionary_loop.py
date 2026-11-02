# Question 9: Write a Python program to iterate
# through a dictionary and print all its keys
# and values.

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

for key, value in student.items():

    print(key, ":", value)