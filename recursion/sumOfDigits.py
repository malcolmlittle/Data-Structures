# How to find the sum of digits of a positive integer number using recursion?
# Basically we are breaking the number down to individual digits so that we can add them 

# f(n) = n % 10 + f(n / 10)

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number has to be a positive integer!'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n / 10))

print(sumOfDigits(3200))