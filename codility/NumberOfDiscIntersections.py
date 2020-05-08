def solution(A):
    pairs = 10000000
    count = 0
    for i in A:
        for y in A[i+1:]:
            print(i,y)
    # for i,j in enumerate(A):        
    #         start = i-j
    #         end = i+j
    #         print(start,end, i, j)
            #string_list.extend([[start,end]])
    #print(string_list)
    # for k, x in enumerate(string_list):
    #     for y in string_list[k+1:]:
    #         #print('47: ', x,y)
    #         if x[-1] >= y[0]:
    #             count = count + 1
    #             if count > pairs:
    #                 count = -1
    #                 break
    # print(count)
    # return count

#solution([1, 2147483647, 0])
#solution([1, 10, 100, 1])  
solution([1,5,2,1,4,0])
#solution( [1, 1, 1])

