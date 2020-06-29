# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    #A
    #[3][2][-6][4][0]
    
    if len(A) == 1:
        return A[0]
    
    front_sum = [0]*len(A)
    back_sum = [0]*len(A)
    current_sum = 0
    
    for i in range(len(A)):
        if A[i] + current_sum > 0:
            front_sum[i] = A[i] + current_sum
            current_sum = A[i] + current_sum
        else:
            front_sum[i] = A[i] + current_sum
            current_sum = 0
    
    current_sum = 0
    
    for i in range(len(A)-1,-1,-1):
        if A[i] + current_sum > 0:
            back_sum[i] = A[i] + current_sum
            current_sum = A[i] + current_sum
        else:
            back_sum[i] = A[i] + current_sum
            current_sum = 0
    
    max_sum = max(A)
    
    for i in range(len(A)-1):
        if front_sum[i] + back_sum[i+1] > max_sum:
            max_sum = front_sum[i] + back_sum[i+1]
            
    return max_sum
        
    
    pass
