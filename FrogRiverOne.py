# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    
    # step 1 - input x,a
    # already succeed
    
    # step 2 - # step 2 - if 1,2,3,.. in arr then, change the index into 0
    # else: continue
    
    check = [0] * X
    check_sum = 0
    
    for i in range(len(A)):
        if check[A[i]-1] == 0:
            check[A[i]-1] = 1
            check_sum += 1
            
            if check_sum == X:
                return i
                
    return -1
        
    pass
