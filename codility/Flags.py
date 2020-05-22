import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks


def solution(A):
    l = len(A)
    count = 0
    stack = []
    for i in range(0, l):
        try:
            if A[i+1] < A[i] > A[i-1]  :  #and A[i]
                print(A[i], A[i+1], A[i-1])
                stack.append(A[i])
        except IndexError:
                'null'
    print(len(set(stack)))
    return count
    peaks, _ = find_peaks(A, height=0)
#solution([1,5,3,4,3,4,1,2,3,4,6,2])
solution([3, 2, 1] )