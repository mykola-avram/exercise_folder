def solution(A):
    l = len(A)           
    Max = [0]*l  
    Min = [0]*l   
    for i in range(0, l):
        Max[i] = i + A[i]
        Min[i] = i - A[i]
    Max.sort()
    Min.sort()
    Range = 0
    count = 0
    for Range in range(0, l):
        while Range < l and Max[Range] >= Min[Range]:
            Range += 1
        count += Range - Range -1
        if count > 10000000:
            return -1
    return count

#solution([1, 2147483647, 0])
#solution([1, 10, 100, 1])  
#solution([1,5,2,1,4,0])
#solution( [1, 1, 1])

