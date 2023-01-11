# import Array module because python doesn't have them built in
from array import *

array1 = array('i', [1, 2, 3, 4, 5, 6])
array2 = array('d', [1.3, 1.5, 1.6])

# Insertion at the beginning of an array is O(n) linear time complexity
array1.insert(0, 23)

# Insertion at the end of an array is O(n) constant time because we provide index and no elements need to shift
array2.insert(3, 2.0)

# Insertion to full array is O(n) linear time complexity because we have to create new array and move our elements to it

# print(array1)
# print(array2)

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(array1)
# The time complexity of traversing an array with one for loop is O(n) linear time
# The space complextity of this operation is O(1) because we don't need an extra location to perform these operations

