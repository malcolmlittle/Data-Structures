# How to find GCD (greatest common divisor) of two numbers using recursion
# GCD is the largest positive integer that divides the numbers without a remainder
# also called gretest common denom, greatest common factor, or highest common factor
# gcd(a, 0) = a
# gcd(a, b) = gcd(b, a mod b)


def gcd(a, b):
    assert int(a) == a and int(b) == b, 'the numbers must be integers'
    if a < 0:               # unintentional case - the constraints
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:              # base case - stopping condition
        return a
    return gcd(b, a % b)    # recursive case - the flow

print(gcd(33, 11))