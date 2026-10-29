
numbers = [30, 10, 20, 10, 40]

# append()
numbers.append(50)
print("Append:", numbers)

# extend()
numbers.extend([60, 70])
print("Extend:", numbers)

# insert()
numbers.insert(1, 15)
print("Insert:", numbers)

# remove()
numbers.remove(10)
print("Remove:", numbers)

# pop()
removed = numbers.pop()
print("Popped item:", removed)
print("After pop:", numbers)

# sort()
numbers.sort()
print("Sorted:", numbers)

# reverse()
numbers.reverse()
print("Reversed:", numbers)

# index()
print("Index of 20:", numbers.index(20))

# count()
print("Count of 10:", numbers.count(10))

# copy()
copied_numbers = numbers.copy()
print("Copied list:", copied_numbers)

# clear()
numbers.clear()
print("Cleared list:", numbers)
