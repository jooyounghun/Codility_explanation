# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # step 1 - sort the array by acsend way
    A = sorted(A)
    
    # step 2 - find the missing one in range 1 ~ len(A)+1
    for i in range(0,len(A)):
        if i+1 != A[i]:
            return i+1
            
    return len(A)+1
            
    pass
