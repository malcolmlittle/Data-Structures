# n! = n*(n-1)*(n-2)*...*2*1
# n! = n * (n - 1)!

def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!' # unintentional case - the constraint
    if n in [0,1]: # base case
        return 1
    else:
        return n * factorial(n - 1) # recursive case - the flow

print(factorial(4))

# 4! = 4*3*2*1=24

# n! = n*(n-1)*(n-2)*...*2*1