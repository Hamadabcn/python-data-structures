# arrays in python are called lists
students = ["Hamada", "Amira", "Yassin", "Frida"] # size of the array 4 # index: 0, 1, 2 (size - 1)

# both lines together have a complexity of O(2)
# the three lines together have a complexity of O(3)
print(students[1]) # this has a complexity of O(1)
print(students[2])
print(students[0])

# time complexity? (performance of an algorithm)
# big O notation for Accessing an array: O(n)