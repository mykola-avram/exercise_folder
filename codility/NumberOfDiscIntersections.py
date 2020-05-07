def solution(A):
    pairs = 10000000
    string_list = []
    count = 0
    for i,j in enumerate(A):
        dia = i+j
        if j == 0: 
            #Range = list(range(i, dia+1))
            Range = list(i, dia+1)
            string_list.append(Range)
            print(Range)

        else: 
            Range = list(range(0, dia+1))
            string_list.append(Range)
            print(Range)

        #print(Range)
    #print(string_list) #---------------------------
    # for k, x in enumerate(string_list):
    #     for y in string_list[k+1:]:
    #         if x != y: 
    #             a_set = set(x) 
    #             b_set = set(y)         
    #             if len(a_set.intersection(b_set)) > 0:
    #                 count = count + 1
    #                 print(a_set, b_set,count) #---------------------------
    # if count < pairs:                 
    #     print(count)
    # else:
    #     print(-1)
    
#solution([1, 10, 100, 1])  
solution([1,5,2,1,4,0])



    # for x in range(0, len(string_list)):
    #     for y in range(x+1, len(string_list)): #) in string_list: 
    #         print(x,y)
    # for x in string_list:
    #     for y in string_list:
    #         print(x,y)
    # for ( var i=0; i<arr.length; i++ ) {
    #     for ( var j= i + 1 ; j<arr.length; j++ ) {
        # console.log(arr[i], arr[j]);
#     }
# }
            #if x == y: #print( x, y) 
                #count = count + 1
                #print(1)
            # else:         