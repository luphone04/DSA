def mergesort(arr):
    if len(arr) > 1:
        left_arr = arr[: len(arr)//2]
        right_arr = arr[len(arr)//2 :]

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


arr_test = [56,34,12,78,43,90,1]
import time
st = time.process_time()
mergesort(arr_test)
et = time.process_time()

print(arr_test)
print(et - st)