#!/usr/bin/python3

#Function to find inversion count of a given list
def findInversionCount(A):
    inversionCount = 0
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                inversionCount += 1

    return inversionCount

if __name__ == '__main__':
    A = [-1, 6, 3, 4, 7, 4]
    print(findInversionCount(A))
