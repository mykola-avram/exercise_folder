def solution(A):    
    result = 0
    for i in A:
        result ^= i
    return result