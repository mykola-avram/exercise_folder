def solution(A):
    # write your code in Python 3.6
    unique_list = [] 
   
    for x in A: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    return len(unique_list)
    
solution([2,1,1,2,3,1,-100])