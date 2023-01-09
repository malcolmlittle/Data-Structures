# What is the runtime of the below code?

def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(array[i] + "," + array[j])

# The runtime in O(n^2)
# The runtime can be determined by counting the iterations or by average work