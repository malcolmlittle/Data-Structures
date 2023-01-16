# import Array module because python doesn't have them built in
from array import *

arr1 = array('i', [2, 4, 6, 8, 10])

def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
        return "The element does not exist in this array"

# The time complexity is O(n)
# The space complexity is O(n)