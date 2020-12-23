# T(n) = O(2n + 1) = O(n)
states = {}


def compute(n):
    if n in states:
        return states[n]

    result = None
    if n == 1 or n == 2:
        result = 1
    else:
        result = compute(n-1) + compute(n-2)

    states[n] = result
    return result
