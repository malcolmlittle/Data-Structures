# How to convert a number from decimal to binary using recursion?
# f(n) = n mod 2 + 10 * f(n/2)

def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be an integer only'     # unintentional case - the constraint
    if n == 0:      # base case - stopping condition to avoid infinite loop
        return 0
    return n % 2 + 10 * decimalToBinary(int(n / 2))     # recursive case - the flow


print(decimalToBinary(44))


# Divide the number by 2
# Get the integer quotient for the next iteration
# Get the remainder for the binary digit
# Repeat the steps until the quotient is equal to 0