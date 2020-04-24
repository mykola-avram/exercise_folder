def solution(A):
    
    l = len(A)+1
    o = l * (l + 1)//2
    return o - sum(A)