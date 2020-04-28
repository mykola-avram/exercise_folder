def solution(N, A):
    l = len(A)
    a = [0] * N
    Max = 0
    count = 0 
    
    for i, el in enumerate(A):   #start = 1
        if (el > N):  
            Max = count
            a = [Max] * N          
           
        else:
             a[el-1] = a[el-1]+1
             Max = a[el-1]
             if(Max > count):
                    count = Max
  
    print(a) 

# def solution(N, A):
#     result = [0]*N    # The list to be returned
#     max_counter = 0   # The used value in previous max_counter command
#     current_max = 0   # The current maximum value of any counter
#     for command in A:
#         if 1 <= command <= N:
#             # increase(X) command
#             if max_counter > result[command-1]:
#                 # lazy write
#                 result[command-1] = max_counter
#             result[command-1] += 1
#             if current_max < result[command-1]:
#                 current_max = result[command-1]
#         else:
#             # max_counter command
#             # just record the current maximum value for later write
#             max_counter = current_max
#     for index in range(0,N):
#         if result[index] < max_counter:
#             # This element has never been used/updated after previous
#             #     max_counter command
#             result[index] = max_counter
#     return result
#https://codesays.com/2014/solution-to-max-counters-by-codility/