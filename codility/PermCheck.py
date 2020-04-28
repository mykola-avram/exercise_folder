def solution(A):
    Max = max(A)
    Min = min(A)
    #A = list(set(A))
    l = len(A)
    if(l == 1 and A[0] == 1):
        print(1)
        return 1
        
    else:
        if Max - Min + 1 == len(A) and Max != Min :
            print(1)
            return 1
        else:
            print(0)
            return 0 
    
solution([3,2])