def Solutio(A):
    ans = 0
    for element in A:
        # XOR operator
        ans = ans ^ element
    return ans
