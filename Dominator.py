# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    half_num_of_arr = int(len(A)/2)
    
    dominator_arr = {}
    
    
    for i in range(len(A)):
        if A[i] in dominator_arr:
            dominator_arr[A[i]].append(i)
        else:
            dominator_arr[A[i]] = [i]
            
    arr = sorted(dominator_arr.items(), key=lambda x: len(x[1]), reverse = True)
    
    try:
        if len(arr[0][1]) > half_num_of_arr:
            return arr[0][1][0]
        else:
            return -1
    except:
        return -1
    
    
    pass
