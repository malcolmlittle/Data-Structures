import numpy as np

# Insertion - Two Dimensional Array
# Time complexity O(mn)
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 1, [[1, 2, 3, 4]], axis=0)
# print(newTwoDArray)

newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

# Accessing an elememnt of Two Dimensional Array
# The time complexity of this is O(1) - Constant time
# The space complexity is also O(1) - Constant time as no extra memory is needed
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect index')
    else:
        print(array[rowIndex][colIndex])

accessElements(twoDArray, 2, 3)


# Traversing through a Two Dimensional Array
# The time complexity of this is O(mn) - if m = n then it will be O(n^2) quadratic time complexity
# The space complexity is O(1) - Constant time as no extra memory is needed
def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseTDArray(twoDArray)


# Searching for an element in a Two Dimensional Array
# The time complexity is O(mn)
# The space complexity is O(1)
def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index '+str(i)+" "+str(j)
    return 'The element is not found'

print(searchTDArray(twoDArray, 14))