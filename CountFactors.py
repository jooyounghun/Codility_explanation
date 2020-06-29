# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    number_iter = 1
    factor_cnt = 0
    
    while number_iter*number_iter < N:
        # 약수이면
        if N/number_iter%1 == 0:
            factor_cnt += 2
            
        number_iter += 1
        
    if number_iter*number_iter == N:
        factor_cnt += 1
        
    return factor_cnt
    pass
