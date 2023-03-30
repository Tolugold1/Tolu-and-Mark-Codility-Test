def Solution(A):
    unique_list = []
    for i in A:
        if i not in unique_list:
            unique_list.append(i)
    print(len(unique_list))