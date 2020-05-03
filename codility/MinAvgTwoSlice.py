# def solution(A):
#     l = len(A)
#     size = 2
#     array = []

#     for i in range(1,l, size):
#         print(A, i, i+2*size)
#         if i+2*size > l:
#             a = sum(A[i:])/len(A[i:])
#             print(a, A[i:], len(A[i:]))
#             array.append([a,i])            
#             break
#         else:
#             a = sum(A[i:i+2])/len(A[i:i+2])
#             array.append([a,i])
#     print(min(array)[1:], array)
#     for i in min(array)[1:]: 
#         print(i)       
    
# #solution([10000, -10000])
# solution([4,2,2,5,1,5,8,9])    

def solution(A):
    l = len(A)
    size = 2
    array = []

    for i in range(1,l, size):
        #print(A, i, i+2*size)
        if i+2*size > l:
            #print(A)
            a = sum(A)/len(A)
            #print(a, A[i:], len(A[i:]))
            print(a)
            array.append([a,i])            
            break
        else:
            a = sum(A[i:i+2])/len(A[i:i+2])
            array.append([a,i])
    print(min(array)[1:], array)
    for i in min(array)[1:]: 
        print(i)       
    
solution([10000, -10000])
#solution([4,2,2,5,1,5,8,9])    