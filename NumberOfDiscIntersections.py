# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    arr = []
    
    for i,v in enumerate(A):
        arr.append((i+v,1))
        arr.append((i-v,-1))
        
    arr.sort()
    
    
    intersect = 0
    intervals = 0
    
    for i,v in enumerate(arr):
        if v[1] == 1:
            intervals -= 1
        if v[1] == -1:
            intersect += intervals
            intervals += 1
    
    if intersect > 10000000:
        return -1
    
    return intersect
    pass
