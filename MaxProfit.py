# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    
    #A
    #23171 21011 21123 21366 21013 21367
    
    #A = [21011,23423,24333,14235,40293,23102]
    
    if len(A) < 2:
        return 0
        
    
    max_sorted_arr = [0]*len(A)
    min_sorted_arr = [0]*len(A)
    
    min_value = A[0]
    max_value = A[-1]
    
    for i in range(len(A)-1):
        if min_value > A[i]:
            min_value = A[i]
        min_sorted_arr[i] = min_value
        
    for i in range(len(A)-1,0,-1):
        if max_value < A[i]:
            max_value = A[i]
        max_sorted_arr[i] = max_value
        
    
    max_profit = 0
    
    for i in range(len(A)-1):
        if max_profit < max_sorted_arr[i+1] - min_sorted_arr[i]:
            max_profit = max_sorted_arr[i+1] - min_sorted_arr[i]
            
    return max_profit
        
        
            
    
        
    pass
