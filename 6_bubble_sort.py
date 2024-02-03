grades = [10, 20, 6, -5, 25, 15, 5, -15] # arrange array to be => [5, 6, 10, 15, 20]
print(grades)

# bubble sort algorithm:

# 1) length of the array
length = len(grades) 

# 2) loop on elements in array
for index in range(0, length - 1):
    for compare in range(0, length - index - 1):
        first = grades[compare]
        second = grades[compare + 1]
        if first > second:
            grades[compare] = second
            grades[compare + 1] = first
        
print(grades)

print("Highest Grade is: " + str(grades[-1]))
print("Lowest Grade is: " + str(grades[0]))