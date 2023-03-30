def solution(A, K):
    if len(A) != 0:
        for i in range(K):
            last_element = A[len(A) - 1]
            A.insert(0, last_element)
            A.pop()
        return A
    else:
        return A