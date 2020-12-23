# T(n) = O(n)
def compute(n):
    if n == 1 or n == 2:
        return 1
    
    states = [None] * (n + 1)
    states[1] = 1
    states[2] = 2
    
    for value in range(1,n):
        if value == 1 or value == 2:
            states[value] = 1
        else:
            states[value] = states[value-1] + states[value - 2]

    return states[n-1] + states[n-2]
