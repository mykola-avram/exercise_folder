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
