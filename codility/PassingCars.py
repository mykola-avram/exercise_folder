def solution(A):
    n = len(A)
    count_of_zero=A.count(0)
    count_of_ones=A.count(1)
    pairs =  1000000000
    if count_of_ones+count_of_zero > pairs:
        return -1
    else:
        return count_of_ones+count_of_zero
    # P = [0] * (n + 1)
    # for k in range(1, n + 1):
    #     P[k] = P[k - 1] + A[k - 1]
    # print(P)
    
    
    #count_total(P, x, y):
    # print(P[count_of_ones + 1] - P[count_of_zero])
    # print(count_of_zero,count_of_ones)

solution([0,1,0,1,1])