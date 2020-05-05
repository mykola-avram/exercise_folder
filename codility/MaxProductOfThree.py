def solution(A):
    result = 1
    A.sort()
    A = A[-3:]
    print(A)
    for i in A: 
         result = result * i
    print(result)
    return result 
    #for 
    
solution([-5, 5, -5, 4])
#solution([-3,1,2,-2,5,6])

