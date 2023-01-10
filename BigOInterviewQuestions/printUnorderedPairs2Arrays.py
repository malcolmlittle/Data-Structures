# What is the runtime of the below code?

def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str[arrayA[i]] + "," + str(arrayB[j]))

# b = len(arrayB)
# a = len(arrayA)

# Therefore the runtime in O(ab)
# This runtime is NOT O(n^2) because the outer and inner loops run thru different arrays