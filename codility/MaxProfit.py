def solution(A):
    # write your code in Python 3.6
    #A.reverse()
    l = len(A)
    if l > 0:
        profit = 0 
        Max = max(A)
        Min = min(A)
        start = A.index(Min)
        print(max(A[start:]) -  min(A), max(A[start:])) 
    else:
        return 0 

#solution([])





