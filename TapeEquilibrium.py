# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    # step 1 - if length of A ==  2
    if len(A) == 2:
        return abs(A[0]-A[1])
        
    # step 2 - create a array
    arr_ = []
    
    tmp_1 = 0
    tmp_2 = sum(A)
    
    # step 3 - get a difference between the sum of two part using iteration
    for i in range(len(A)-1):
        tmp_1 = tmp_1 + A[i]
        tmp_2 = tmp_2 - A[i]
        arr_.append(abs(tmp_1 - tmp_2))
        
        
    return min(arr_)
        
        
    pass
