# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    
    if len(A) == 1:
        return 1
    
    arr = []
    
    for i in range(len(A)):
        arr.append((A[i],B[i]))
        
    arr_ = []
    arr_.append(arr[0])

    for i in range(1,len(arr)):
        
        # 충돌하면
        while(True):
            if arr[i][1] == 0 and arr_[len(arr_)-1][1] == 1:
                # 기존 물고기가 더 쎄면
                if arr[i][0] < arr_[len(arr_)-1][0]:
                    break
                # 새로운 물고기가 더 쎄면
                else:
                    del arr_[len(arr_)-1]
                    if len(arr_) == 0:
                        arr_.append(arr[i])
                        break
            else:
                arr_.append(arr[i])
                break
            
    return len(arr_)
            
    pass
