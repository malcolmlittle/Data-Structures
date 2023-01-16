from array import *

arr1 = array('i', [2, 4, 6, 8, 10, 12])

# use the remove method to get rid of the first occurence of specified value
arr1.remove(6)

print(arr1)

# The time complexity is O(n) - linear
# The space complexity is O(1) - constant