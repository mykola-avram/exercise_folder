def solution(X, A):
        array = set()
        for i,j in enumerate(A):
            array.add(j)
            #print(array.add(j), j, i)
            if len(array) == X:
                return i 
        return - 1
                                
#solution(2 , [2, 2, 2, 2, 2])
#solution(3, [1,3,4,2,3,4,5,6])
solution(5, [1,3,1,4,2,3,5,4])
#solution(1, [1])
#solution(5, [3])
