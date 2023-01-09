# What is the runtime of the below code?

def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))

# The runtime in O(n^2)