def solution(A):
    pairs = 10000000
    string_list = []
    count = 0
    for i,j in enumerate(A):
        start = i-j
        end = i+j
        string_list.extend([[start,end]])
    #print(string_list)
    for k, x in enumerate(string_list):
        for y in string_list[k+1:]:
            #print('47: ', x,y)
            if x[-1] >= y[0]:
                count = count + 1
                if count > pairs:
                    count = -1
                    break
    print(count)
    return count
            #a = list(map(int, str(x[0]))) if x[0] == x[-1] else list(range(x[0],x[-1]+1,1))
            #b = list(map(int, str(y[0]))) if y[0] == y[-1] else list(range(y[0],y[-1]+1,1))
            #print(a, b)
    #         xs = set(a)
    #         if xs.intersection(b):  
    #             count = count + 1
    #             if count > pairs:
    #                 count = -1
    #                 break
    #                 #print(count)
    # #print(count)
    # return count            

#solution([1, 2147483647, 0])
#solution([1, 10, 100, 1])  
#solution([1,5,2,1,4,0])
solution( [1, 1, 1])

