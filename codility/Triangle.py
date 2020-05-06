def solution (A):
    A = sorted(A, reverse=True)
    if len(A) >= 3:
        offsets =  A, A[1:], A[2:]
        for value in list(zip(*offsets)):
            l = list(value)        
            Max = sum(l[:1])
            Max_2 = sum(l[1:]) 
            if Max < Max_2:
                return 1
                break
        return 0
    else:
        return 0
    
#solution([10, 50, 5, 1])
#solution([0,1,2,3,4,5]) 
# is triangular if 0 ≤ P < Q < R < N      5 8 10
# 1 10 5
# P Q R 
# 5 1 
# 1 1 5  
# A[P] + A[Q] > A[R],
# A[Q] + A[R] > A[P],
# A[R] + A[P] > A[Q].
# For example, consider array A such that:

#   A[0] = 10    A[1] = 2    A[2] = 5
#   A[3] = 1     A[4] = 8    A[5] = 20