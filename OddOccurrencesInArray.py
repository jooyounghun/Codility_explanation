# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    
    # step 1 - make a dictionary
    dict_= {}
    
    # step 2 - fill the dictionary
    for i in A:
        try: 
            dict_[i] += 1
        except: 
            dict_[i] =1
    
    # step 3 - find the odd value
    for i in dict_:
        if dict_[i] % 2 == 1:
            return i
    
    pass
