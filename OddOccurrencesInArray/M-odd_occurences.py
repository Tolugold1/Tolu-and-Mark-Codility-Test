def Solution(A):
    # sort the array in ascending order
    A = sorted(A)
    # check for extreme single test i.e A = [54]
    if len(A) == 1:
        return A[0]
    # iterate in units of two then check the paired elements
    for i in range(0, len(A), 2):
        if A[i] != A[i + 1]:
            return A[i]
