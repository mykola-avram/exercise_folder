def solution(S, P, Q):  
    key = {'A':1, 'C':2, 'G':3, 'T':4}
    arr = []
    for i in [slice(start, end+1) 
        for start, end in zip(P,Q)]:
            arr.append(key[min(S[i])])
    return arr