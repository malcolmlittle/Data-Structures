# What is the runtime of the below code?

def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):
                print(str[arrayA[i]] + "," + str(arrayB[j]))

# b = len(arrayB)
# a = len(arrayA)

# 100000 units of work is still constant
# This runtime is O(ab)