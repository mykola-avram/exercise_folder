
def solution(A): 
    n = len(A)

    for i in range(n) : 
  
 
        if (arr[i] <= 0 or arr[i] > n): 
            continue
  
        val = arr[i] 

        while (arr[val - 1] != val): 
            nextval = arr[val - 1] 
            arr[val - 1] = val 
            val = nextval 
            if (val <= 0 or val > n): 
                break
  
    for i in range(n): 
        if (arr[i] != i + 1) : 
            return i + 1
  
    return n + 1
