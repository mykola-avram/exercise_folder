def solution(A): 
    l = len(A) 
    if l > 0:  
        max_diff = A[1] - A[0] 
        min_element = A[0] 
        for i in range( 1, l ): 
            if (A[i] - min_element > max_diff): 
                max_diff = A[i] - min_element 

            if (A[i] < min_element): 
                min_element = A[i] 
        return max_diff 
    else:
        return 0  
# Driver program to test above function  
#solution([])





