def solution(A: list)-> int:
    """Return smallest positive number greater than 0 and not in A"""
    max_num = max(A)
    if max_num > 0:
        intergers_not_in_A = [i for i in range(1, 100001) if i not in A]
        result = min(intergers_not_in_A)
        return result
    else:
        return 1
