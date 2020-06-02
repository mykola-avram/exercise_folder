def solution(A):
    pairs =  1000000000
    cars = 0
    cross = 0
    for i in A:
        if i == 0:
            cars += 1
        else:
            cross += cars
            if cross > pairs:
                return -1
    print(cross)
solution([0,1,0,1,1])
