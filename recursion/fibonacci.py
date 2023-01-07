# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    assert n >= 0 and int(n) == n, 'fibonacci number cannot be negative number or non integer'  # unintentional caase - the constraint
    if n in [0, 1]: # base case
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # recursive case - the flow

print(fibonacci(9))

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89…