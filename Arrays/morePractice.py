from array import *

# 1. Create an array and traverse

my_array = array('i', [1, 2, 3, 4, 5])

for i in my_array:
    print(i)


# 2. Access individual elements through indexes

print("Step 2")
print(my_array[0])

# 3. Append any value in an array using insert() method
print("Step 3")
my_array.append(6)
print(my_array)

# 4. Insert value in an array using insert method
print("Step 4")
my_array.insert(0, 11)
print(my_array)

# 5. Extend python array using extend() method
