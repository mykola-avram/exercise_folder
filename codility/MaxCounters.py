def solution(N, A):
    l = len(A)
    a = [0] * N
    Max = 0
    count = 0 
    
    for i, el in enumerate(A):   #start = 1
        #print ('8: ',i, el)
        if (el > N):  
            #Max = max(a)
            Max = count
            #print('max.16..', Max)
            a = [Max] * N          
            # for x in a:
            #      if x > Max:
            #          Max = x
            #print('sdfsdf',Max)
            #print('19 ',a)
            
        else:
             a[el-1] = a[el-1]+1
             Max = a[el-1]
             #count = Max
             #print('sdfsdf',Max)
             #print('25: ', Max, count)
             if(Max > count):
                    count = Max
                    #print('max_count:', Max, count)
  
    
    print(a) 

#solution(5, [3,4,4,6,1,4,4])
solution (1, [2, 1, 1, 2, 1])
#solution (6, [1,2,3,1,1,5,7,8])
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