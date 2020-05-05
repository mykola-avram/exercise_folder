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
