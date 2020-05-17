def solution(A):
    max_ending, max_slice = 0,0
    l = len(A)
    if l > 1:
        if all(i < 0 for i in A):
            return max(A)
        else:
            for a in A:
                max_ending = max(0, max_ending + a)
                max_slice = max(max_slice, max_ending)
            return max_slice
    else:
        for i in A:
            return i

#solution([3 ,2 ,-6, 4  ,0])
#solution([0])
#solution([-3,-2])