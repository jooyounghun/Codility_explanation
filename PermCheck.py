# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # step 1 - get input A
    # already succeed
    
    # step 2 - sorting A, which is consist of positive integer
    A = sorted(A)
    
    # step 3 - do the job(for sentence)
    a = 1
    
    for i in A:
        if i == a:
            a += 1
        else:
            return 0
            
    return 1
    
    
    pass
