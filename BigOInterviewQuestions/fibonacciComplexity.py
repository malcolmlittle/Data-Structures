# What is the runtime of the below code?

def allFib(n):
    for i in range(n):
        print(str(i)+ ":, " + str(fib(i)))
    
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# remember that recursive algorithms that make multiple calls take runtime O(branches^depth)
# branches are the number of children whih is the number of calls, and depth is the param that we are passing
# so our second function will have runtime of O(2^n)