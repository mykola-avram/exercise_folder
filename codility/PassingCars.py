def solution(A):
    l = len(A)
    pairs =  1000000000
    count_of_zero = 0
    for i, y in enumerate(A):
        if y == 0 and l != 1:           
            count_of_zero += A[i:].count(1)
            #print(count_of_zero)
    if count_of_zero > pairs:
          return -1
    else:
          return count_of_zero
 
solution([0,1,0,1,1])