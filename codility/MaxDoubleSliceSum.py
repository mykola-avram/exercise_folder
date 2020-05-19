def solution(A):

    l = len(A)
    sum_i = [0] * l
    i_sum = [0] * l

    for index in range(1, l - 2):  # A[X + 1] + A[X + 2] + ... + A[Y - 1]
        print(index)
        sum_i[index] = max(sum_i[index - 1] + A[index], 0)

    for index in range(l - 2, 1, -1):  # A[Y + 1] + A[Y + 2] + ... + A[Z - 1]
        print(index)
        i_sum[index] = max(i_sum[index + 1] + A[index], 0)

    max_slice_sum = sum_i[0] + i_sum[2]
    for index in range(1, l - 1):
        print(index)
        max_slice_sum = max(max_slice_sum, sum_i[index - 1] + i_sum[index + 1])
        print(max_slice_sum)

    return max_slice_sum
