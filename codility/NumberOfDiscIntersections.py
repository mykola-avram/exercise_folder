def solution(A):
    l = len(A)           
    Max = [0]*l  
    Min = [0]*l   
    for i in range(0, l):
        Max[i] = i + A[i]
        Min[i] = i - A[i]
    Max.sort()
    Min.sort()
    range_lower_index = 0
    count = 0
    for Range in range(0, l):
        while range_lower_index < l and Max[Range] >= Min[range_lower_index]:
            range_lower_index += 1
        count += range_lower_index - Range -1
        if count > 10000000:
            return -1
    return count

#solution([1, 2147483647, 0])
#solution([1, 10, 100, 1])  
#solution([1,5,2,1,4,0])
#solution( [1, 1, 1])

