def solution(A, K):
    # if the size of k > len(a), rotate only necessary with
    # module of the division
    try:
       rotations = K % len(A)
    except ZeroDivisionError:
        rotations = 0 
    #print(rotations)
    return A[-rotations:] + A[:-rotations]