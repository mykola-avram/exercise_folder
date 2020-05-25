def solution(A):
    l = len(A)
    stack = []
    for i in range(0, l):
        len_of_sa = len(A[i+1:]+A[:i])
        tmp_list =A[i+1:] + A[:i]
        count = 0
        for j in range(0, len(tmp_list)):
            if A[i] % tmp_list[j] != 0:
                count+= 1
        stack.append(count)
    print(stack)

solution([3, 1, 2, 3, 6])