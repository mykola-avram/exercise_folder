def solution(A, B):
    offsets =  A, B
    stack_0, stack_1 = [],[]
    for start, end in zip(*offsets): 
        if end == 1:
            stack_1.append(start)
        else:
            stack_0.append(start)
    Max_0 = max(stack_0)
    Max_1 = max(stack_1)
    #print(stack_0, stack_1, Max_0, Max_1) 
    if Max_0 > Max_1:
        stack_0 = sorted(stack_0,reverse=True)
        j2 = [i for i in stack_0 if i >= Max_1]
        return len(j2)
    else:
        stack_1 = sorted(stack_1, reverse=False)
        j2 = [i for i in stack_1 if i >= Max_0]
        return len(j2)