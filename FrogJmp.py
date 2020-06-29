# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    
    # step 1 - 방정식 문제로 풀 수 있겠다
    
    ########################
    # frog X >= frog Y
    # a를 구하면 되는 문제
    
    # X+a*D >= Y
    # a*D >= Y - X
    # a >= (Y - X)/D
    # ex) (85 - 10)/30
    # ex) (75)/30 = 2.5
    ########################
    
    
    a = (Y - X) / D
    
    # 딱 맞아떨어지면, int() 내장 함수를 써서, 2.0 -> 2로 변환 후 반환해줌
    if a % 1 == 0:
        return int(a)
    # 2.4 이렇게 소수로 떨어지면 int()를 통해 정수로 변환하는 '버림'을 하고 2로 만든 후 +1 해서 반환 
    else:
        return int(tmp) + 1
    
    
    pass
