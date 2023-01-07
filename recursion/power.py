# How to calculate power of a number using recursion?
# x^n = x * x^n-1

def power(base, exponent):
    assert int(exponent) == exponent, 'The exponent must be integer number only'
    if exponent == 0: # base case - stopping criterion to avoid infinite loop
        return 1
    elif exponent < 0: # unintentional case - the constraint
        return 1 / base * power(base, exponent + 1)
    else:
        return base * power(base, exponent - 1) # recursive case - the flow

print(power(2, 4))

# 2^4 = 2*2*2*2
# x^a * x^b = x^a+b
# x^3 * x^4 = x^3+4
# x^n = x * x^n-1

