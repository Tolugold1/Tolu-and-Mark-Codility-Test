def solution(A):
    ans = 0
    for i in range(0, len(A)): #loop through the length of A from 0
        for j in range(i + 1, len(A)):  #loop through the length of A starting from the index after i
            if (A[i] > A[j]):  # check if value at index i is greater that the value at index j
                ans += 1  # if true, increment the value of ans
    return ans  # return ans


print(solution([-1, 6, 3, 4, 7, 4]))