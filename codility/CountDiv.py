def solution(A, B, K):
    output = []
    #print(A, B)
    for el in range(A,B+1):   
        if(el%K==0) :           
            output.append(el)
        #temp = temp // 10
    print(len(output))
solution(1, 1, 11)