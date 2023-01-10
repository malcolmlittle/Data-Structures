# What is the runtime of the below code?

def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        # remember the factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)

# The runtime is O(n) - linear