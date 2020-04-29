def solution(A):
    Max = max(A)
    Min = min(A)
    A.sort()
    l = len(A)   
    if(A[0] == 1 and l == 1 ):
        return 1              
    else:
        if Max - Min + 1 == l and A[0] == 1 and l == len(set(A)):
            return 1
        else:
            return 0 
        return 0 
#solution([9, 5, 7, 4, 2, 6, 3, 1, 10, 8])