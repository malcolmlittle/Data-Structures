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
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect index')
    else:
        print(array[rowIndex][colIndex])

accessElements(twoDArray, 2, 3)