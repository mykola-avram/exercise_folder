def solution(N):
        A = B = 0
        stack = [2 * (N + N), 2 * (N + N)]
        if N != 1:
            for i in range(1, N):
                if N % i == 0:
                    B = N // i
                    C = 2 * (i + B)
                    stack.append(C)
                    if C > stack[-2]:
                        break
            return stack[-2]
        else:
            return 4
