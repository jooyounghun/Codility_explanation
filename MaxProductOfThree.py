# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    A = sorted(A, reverse=True)
    
    if A[0]*A[1]*A[2] > A[0]*A[-1]*A[-2]:
        return A[0]*A[1]*A[2]
    else:
        return A[0]*A[-1]*A[-2]
    
    pass
