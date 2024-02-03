# binary search is much faster than linear search because it cuts the array in half but it down side is
# that the array has to be sorted

def binarySearch(array, search, lowIndex, highIndex):
    
    while lowIndex <= highIndex:
        mid = lowIndex + (highIndex - lowIndex) // 2 # floor(//) gets you to the right number from down not up
        
        if array[mid] == search:
            return mid
        
        elif array[mid] < search:
            lowIndex = mid + 1
            
        else:
            highIndex = mid - 1
        
    return -1 # -1 means element is not found

# sorted array very important for binary search it cannot be done if not       
grades = [10, 12, 14, 15, 17, 19 , 20] # length of 7
search = 19

result = binarySearch(grades, search, 0, len(grades) - 1)

if result == -1:
    print("Not Found")
else: 
    print("Found")

# best case O(1) if it was number 10
# worst case O(n) => O(7) if it was number 20

# imagine there were 1000 elements in the array O(1000) not logical!!!
# binary search can fix that on contrast of the linear search
# divide and conquer, which means it cuts the array in half and then searches for the given number
# but the arrays have to be in order

# binary search O(log n) algorithm