# What is the runtime of the below code?

def powersOf2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOf2(int(n / 2))
        curr = prev * 2
        print(curr)
        return curr

# The runtime is O(log n)