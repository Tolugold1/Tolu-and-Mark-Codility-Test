def solution(A: list)-> int:
    """Return smallest positive number greater than 0 and not in A"""
    for i in range(len(A)):
        if A[i] < 0:
            min_num = "lt-0"
        else:
            min_num = 'gt-0'
    if min_num == 'gt-0':
        intergers_not_in_A = [i for i in range(1, 100001) if i not in A]
        result = min(intergers_not_in_A)
        return result
    else:
        return 1
