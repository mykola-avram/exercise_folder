# def solution(a_list):
#     #b = []
#     results = []
#     for i in range(1,len(a_list)):
#         #b.append(sum(a_list[:i+1]))
#         results.append(abs(sum( a_list[:i+1]) - sum(a_list[i+1:])))
# solution([3, 1, 2,  4, 3])
# solution(list(range(-1000, 1000))) 

def solution(A):
    l = A[0]  
    r = sum(A[1::])    
    diff = abs(l - r)
 
    for p in range(1, len(A)):
        ldiff = abs(l - r)
        if ldiff < diff:
            diff = ldiff
        l += A[p]        
        r -= A[p]
    return diff
    
#solution([3, 1, 2,  4, 3])