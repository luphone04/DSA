def mergesort(arr):
    if len(arr) > 1:
        leftarr = arr[:len(arr)// 2 ] 
        rightarr = arr[len(arr)//2 : ]

        #recursion
        mergesort(leftarr)
        mergesort(rightarr)
        i = 0
        j = 0
        k = 0
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
            else:
                arr[k] = rightarr[j]
                j += 1

            k += 1
        while i < len(leftarr):
            arr[k] = leftarr[i]
            i += 1
            k += 1
        while j < len(rightarr):
            arr[k] = rightarr[j]
            j += 1
            k += 1
arr_test = [4 ,56,86, 54,96,26,75,33,65,76]
import time

st = time.process_time()
mergesort(arr_test)
et = time.process_time()
print(arr_test)
print(et - st)