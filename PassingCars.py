# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    east_car_num = 1
    
    passing_car_num = 0
    
    # 최초 동쪽으로 가는 차 위치
    try:
    # 동쪽으로 가는 차가 없으면 에러 발생하여 passing_car가 없으므로 return 0
        east_car = A.index(0)
    except:
        return 0
        
    for i in range(east_car+1,len(A)):
        if A[i] == 1:
            passing_car_num += east_car_num
            
            if passing_car_num > 1000000000:
                return -1
        else:
            east_car_num += 1
            
            
    return passing_car_num
    
    
    pass
