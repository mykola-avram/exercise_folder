def solution(A):
    A.sort()
    #----Min--------
    Min_1 = min(A)
    s = sorted(A)
    Min_2 = s[1]
    Min_3 = s[2]   
    #---Max--------
    Max_1 = max(A)
    o = sorted(A)
    Max_2 = o[-2]
    Max_3 = o[-3]
    b = Max_1 * Max_2 * Max_3
    if all(i < 0 for i in A):
        return b 
    else:
        a = Min_1 * Min_2 * Max_1
        b = Max_1 * Max_2 * Max_3
        if b > a:
            return b
        else:     
            return a
