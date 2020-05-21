def solution(N):
        A = B = 0
        stack = [2 * (N + N), 2 * (N + N)]
        if N != 1:
            for i in range(1, N):
                if N % i == 0:
                    B = N // i
                    C = 2 * (i + B)
                    stack.append(C)
                    #print(stack[-2], C, stack)
                    if C > stack[-2]:
                        break
            print('C: ', stack[-2])
            return C
        else:
            return 4

#solution(30)