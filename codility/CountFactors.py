def solution(n):
    i = 1
    result = 0
    while (i * i < n):
        if (n % i == 0):
            result += 2
        i += 1
    if (i * i == n):
        result += 1
    print(result)
    return result

solution(24)
