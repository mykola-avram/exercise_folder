def solution(N, A):
    l = len(A)
    a = [0] * N
    for i, el in enumerate(A):   #start = 1
        
        if (el > N): 
            #Max = max(a)
            #Max = a[el:el]
            Max = a[0]
            # for x in a:
            #      if x > Max:
            #          Max = x
            #print('sdfsdf',Max)
            a = [Max] * N
        else:
            a[el-1] = a[el-1]+1
            Max = a[el-1]
            #print('sdfsdf',Max)
    
    print(a) 

solution(5, [3,4,4,6,1,4,4])
#solution (1, [2, 1, 1, 2, 1])

    # (3, 2, 2, 4, 2)
    
    

# def solution(N, A):
#     l = len(A)
#     a = [0] * N
#     #Max = max(a)
#     for i, el in enumerate(A):   #start = 1
#         if (el > N):
#             Max = max(a)
#             a = [Max] * N
#         else:
#             a[el-1] = a[el-1]+1
#             #Max = a[el-1]
    
#     #print(a) 
#     return a

# #solution(5, [3,4,4,6,1,4,4])
# #solution(1, [2, 1, 1, 2, 1])