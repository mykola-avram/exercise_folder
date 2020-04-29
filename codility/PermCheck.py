def solution(A):
    Max = max(A)
    Min = min(A)
    A.sort()
    #print(A)
    l = len(A)
    
    if(A[0] == 1 and l == 1 ):
        print('sdf',1)
        return 1
               
    else:
        if Max - Min + 1 == l and A[0] == 1:
            print('sdsf', 1)
            return 1
        else:
            print(0)
            return 0 
        print(0)
        return 0 

    
solution([4,3,1,2])