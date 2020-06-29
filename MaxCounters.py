# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(N, A):
    # write your code in Python 3.6
    
    # step 1 - input N,A
    # already succeed
    
    # step 2 - get for setence
    counters = N * [0]
    next_max_counter =  max_counter = 0
    
    for oper in A:
        try:
            current_counter = counters[oper-1] = max(counters[oper-1] +1, max_counter+1)
            next_max_counter = max(current_counter, next_max_counter)
        except:
            max_counter = next_max_counter
    
    
    return [c if c > max_counter else max_counter for c in counters]
    
    
    pass
