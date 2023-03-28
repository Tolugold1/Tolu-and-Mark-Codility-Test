def Solution(A):
    max_num = max(A)
    possible_numbers = set(range(1, max_num + 2))
    difference = possible_numbers - set(A)
    if len(difference) > 0:
        return min(difference)
    elif max_num < 0: return 1

Solution([1, 3, 6, 4, 1, 2])
