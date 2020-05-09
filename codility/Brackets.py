def solution(S):
    stack = [] 
    for char in S: 
        if char in ["(", "{", "["]:  
            stack.append(char) 
        else: 
            if not stack: 
                return -1
            current_char = stack.pop() 
            if current_char == '(': 
                if char != ")":
                    return -1
            if current_char == '{': 
                if char != "}": 
                    print(-1)
                    return -1
            if current_char == '[': 
                if char != "]": 
                    print(-1)
                    return -1 
    if stack: 
        return False
    return True
#solution("{[()()]}")
#solution("([)()]")
#solution("(U)")