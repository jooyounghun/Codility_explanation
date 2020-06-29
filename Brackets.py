# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    
    
    if len(S) == 0:
        return 1
    
    arr = []
    
    for i in S:
        if i == "{":
            arr.append(3)
        elif i == "[":
            arr.append(2)
        elif i == "(":
            arr.append(1)
        elif i == ")":
            arr.append(-1)
        elif i == "]":
            arr.append(-2)
        elif i == "}":
            arr.append(-3)
           
    
    arr_ = []
    arr_.append(arr[0])
    
    for i in range(1,len(arr)):
        if len(arr_) != 0 and arr[i] < 0 and arr[i] == -1 * arr_[len(arr_)-1]:
            del arr_[len(arr_)-1]
        else:
            arr_.append(arr[i])
        
    if len(arr_) == 0:
        return 1
    else:
        return 0
        
    
    pass
