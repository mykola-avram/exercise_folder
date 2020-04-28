def solution(A):
    Max = max(A)
    Min = min(A)
    #A = list(set(A))
    if Max - Min + 1 == len(A):
        return 1
    else:
        return 0 
    
solution([4,1,3,2])