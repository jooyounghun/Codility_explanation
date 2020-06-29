# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # step 1 - input array A
    # already succeed
    
    # step 2 - find the smallest positive integer of A
    
    # sorting A
    A = set(A)
    A = sorted(A)
    
    # find the positive integer
    try:
        a = A.index(1)
        tmp = A[a:]
    except:
        return 1
        
    b = 1
    
    for i in tmp:
        if i == b:
            b += 1
        else:
            return b
            
    return b
        
    
    pass
