# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    
    arr = []
    
    for i in range(len(S)):
        if S[i] == '(':
            arr.append(S[i])
        else:
            if len(arr) != 0 and arr[-1] == '(':
                del arr[-1]
            else:
                arr.append(S[i])
            
    
    if len(arr) == 0:
        return 1
    else:
        return 0
    
    pass
