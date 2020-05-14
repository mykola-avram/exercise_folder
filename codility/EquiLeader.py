def leader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            value = A[k]
            #print('8:',value, A[k], size)
        else:
            if (value != A[k]):
                size -= 1
                #print('12:','value:',value, 'A[k]:',A[k],'size:', size)
            else:
                size += 1
                #print('15:','value:',value, 'A[k]:',A[k], 'size:',size)
    #print(size,value)
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in range(n):
        if (A[k] == candidate):
            count += 1
    if (count > n // 2):
        leader = candidate   
    return leader 
    #print(leader)
#solution([3,4])


def solution(A):
    l = len(A)
    count = 0
    
    for i in range(1, l):
            #print(A[:i], A[i:], i)
            if leader(A[:i]) == leader(A[i:]):  
                count +=1
    return count
    #print(count)