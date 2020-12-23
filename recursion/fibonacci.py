
# T(n) == O(2^n)
def compute(n):
    if n == 1 or n == 2:
        return 1

    return compute(n-1) + compute(n-2)