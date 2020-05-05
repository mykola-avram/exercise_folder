def solution(A):
    result = 1
    A.sort()
    print(A)
    D = min(A)
    s = sorted(A)
    F = s[1]
    #---------
    M = max(A)
    o = sorted(A)
    print(o)
    K = o[-2]
    #---------
    C = A[-3:]
    B = A[:2]
    print(B, C, D, F, M, K)
    if D * F > M * K:
        temp = D*F
        temp = temp* max(A)
        print('temp:', temp)
    else:
        for i in C: 
            result = result * i
        print(result)
        return result 
    #for 
    
#solution([-5, 5, -5, 4])
#solution([-3,1,2,-2,5,6])
solution([-5,-5,1,2,3,4])

