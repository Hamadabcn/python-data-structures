def linearSearch(array, query):
    for index in range(0, len(array)):
        if array[index] == query:
            return index
    return -1

grades =  [3, 5, 12, 10, 4]
search = 11
result = linearSearch(grades, search)

if result == -1:
    print("Not Found")
else: 
    print("Found")
