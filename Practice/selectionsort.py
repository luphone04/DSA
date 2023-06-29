# [2, 3, 4, 6, 7, 12, 23, 77]
# 4.400000000000237e-05
import time 
st = time.process_time()

def selectionsort(arr):
    for i in range(0, len(arr) - 1):
        min_value = i
        for j in range(i + 1 , len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        if min_value != i:
            arr[min_value] , arr[i] = arr[i] , arr[min_value]
    return arr
print(selectionsort([4,6,2,12,7,23,77,3])) 
et = time.process_time()
print(et - st)