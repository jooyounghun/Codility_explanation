# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    
    start_num = A/K
    end_num = int(B/K)
    
    if start_num%1 != 0:
        start_num = int(start_num) + 1
    else:
        start_num = int(start_num)
    
        
    return end_num - (start_num-1)
    pass
