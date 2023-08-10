def partition(start, end):
    global arr

    pivot = arr[end]
    i = start-1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[end], arr[i+1] = arr[i+1], arr[end]
    return i+1


def quicksort(start, end):
    global arr
    if start < end:
        partition_pos = partition(start, end)
        print(arr[start:partition_pos], arr[partition_pos], arr[partition_pos+1:end+1])
        quicksort(start, partition_pos-1)
        quicksort(partition_pos+1, end)

arr = [8,4,3,1,6,7,11,9,2,10,5]
n = len(arr)

quicksort(0, n-1)
print(arr)