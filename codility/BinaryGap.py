def solution(N):
    a = bin(N)[2:]
    count = 0
    max_count = 0 
    a = str(a).strip('0')
    if a.count('1') == 1:
        max_count = 0
    else:
        for number, item in enumerate(a):  
            if(a[number] == '0'):
                count = count + 1
            else: 
                count = 0
            if(count > max_count):
                max_count = count
    return max_count;