# 4 6 2 12 7 23 77 3
# [2, 3, 4, 6, 7, 12, 23, 77]
# 0.00023100000000000204


def mergesort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #recursion
        mergesort(left_arr)
        mergesort(right_arr)

        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
import time 
a = list(map(int, input().split()))

st = time.process_time()
mergesort(a)
et = time.process_time()
print(a)
print(et - st)









