def solution(S, P, Q):
    
    a = []
    A, C, G, T = 1,2,3,4
    for i,j in zip(P,Q):
        print(i,j)
        p = i    #2
        q = j   #4
        array = []
        for el in S[p:q+1]:
            #print(S[p], S[q])
            if el == 'A':
                array.append(A)
            elif el == 'C':
                array.append(C)
            elif el == 'G':
                array.append(G)
            elif el == 'T':
                array.append(T)
                print(T)
        
        a.append(min(array))
    print(a)
        
solution('CAGCCT',[2,5,0],[4,5,6])