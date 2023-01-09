# What is the runtime of the below code?

def foo(array):
    sum = 0
    product = 1

    for i in array:
        sum += i

    for i in array:
        product += 1
    print("Sum = " + str(sum)+", Product = "+str(product))

# The runtime in O(n)