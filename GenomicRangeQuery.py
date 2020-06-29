# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    
    # step 1 - input array S,P,Q
    # already succeed
    
    # step 2 - get range from array P,Q
    M = len(P)
    
    return_arr = []
    
    # step 3 - do the job(for senetence)
    for i in range(M):
        arr = S[P[i]:Q[i]+1]
        try:
            arr.index('A')
            return_arr.append(1)
        except:
            try:
                arr.index('C')
                return_arr.append(2)
            except:
                try:
                    arr.index('G')
                    return_arr.append(3)
                except:
                    return_arr.append(4)
                    
    return return_arr
        
    pass
