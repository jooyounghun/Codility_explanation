# you can write to stdout for debugging purposes, e.g.  
# print("this is a debug message")  
  
def solution(A, K):  
    # write your code in Python 3.6  
      
    # step 1 - take input A,K  
    # already succeed  
      
    # step 2 - create new array  
    arr_ = list(range(len(A)))  
      
    # step 3 - take iteration to solve the prob
    for i in range(len(A)):  
        arr_[(i+K)%len(A)] = A[i]  
      
    return arr_
    pass
