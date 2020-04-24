def solution(X, Y, D):
    distance = Y - X;
    jumps = distance / D;
    return(distance - 1) // D + 1