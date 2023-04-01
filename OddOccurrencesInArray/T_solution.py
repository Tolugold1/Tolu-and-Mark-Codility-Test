def solution(A):
    for i in A:
        # check if the total number of an element modulo 2 is 1 
        # or if the number of an element is 1
        if A.count(i) % 2 == 1 or A.count(i) == 1:
            return i