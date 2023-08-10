
def partition(A, p, r):  # Lomuto's partition scheme
    x = A[r] # last pivot     #pivot is a special element used for comparison during the sorting process
    i = p-1 # will be using to track the index of smaller element 
    # set it to p-1 initially because there are no smaller elements before the starting index

    for j in range(p, r): #excluding the pivot element
        if A[j] <= x: # if current element is smaller than or equal to pivot
            i += 1 # increment index of smaller element
            # increment i and swap the current element with the element at index i
            A[i],A[j] = A[j],A[i] # swap
    #After the loop finishes, we have divided the subarray into two parts: one with elements smaller 
    # than or equal to the pivot, and one with elements greater than the pivot.

    A[r],A[i+1] = A[i+1],A[r] # swap pivot with element at index i+1 
    # to position the pivot at the correct place

    # because it will be used to divide the subarray further in the quicksort function
    return i+1 # return index of pivot

def quicksort(A, p, r): 
    if p < r:  # If it is, it means there is more than one element in the subarray, and we need to sort it
        q = partition(A, p, r)  #index of the pivot
        quicksort(A, p, q-1)   #excluding the pivot , left subarray 
        quicksort(A, q+1, r) #the right subarray , excluding the pivot





arr = [8,4,3,1,6,7,11,9,2,10,5]

quicksort(arr , 0 , len(arr) - 1)
print(arr)

# pivotIndex = partition(arr,0,len(arr)-1)
# print(pivotIndex)
# print(arr, end="\n")
# arr = [59,37,27,58,433,284,1]
# pivotIndex = partition(arr,0,len(arr)-1)
# print(pivotIndex)
# print(arr, end="\n")

# arr = [1,2,3,4,5]
# pivotIndex = partition(arr,0,len(arr)-1)
# print(pivotIndex)
# print(arr)

# arr = [1,2,3,5,6,7,4]
# pivotIndex = partition(arr,0,len(arr)-1)
# print(pivotIndex)
# print(arr)




