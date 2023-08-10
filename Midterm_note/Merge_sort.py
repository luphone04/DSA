def merge(A, p, q, r):
    B = [] # temporary array
    i = p # left array index
    j = q+1 # right array index
    while i <= q and j <= r: # running time is O(n) because it is only one loop and it is not nested inside another loop so it is O(n)
        if A[i] <= A[j]: # running time is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1)
            B.append(A[i]) # running time is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1)
            i += 1 # running time is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1)
        else: # running time is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1)
            B.append(A[j]) # running time is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1)
            j += 1 # running time is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1)
    A[p:r+1] = B + A[i:q+1] + A[j:r+1] # running time is O(n) because it is only one loop and it is not nested inside another loop so it is O(n)

def mergesort(A, p, r): # running time is O(nlogn) because the while loop is inside the for loop and the while loop is also inside the while loop so the running time is O(nlogn)
    if p < r: # running time is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1)
        q = (p+r)//2 
        mergesort(A, p, q) # running time is O(nlogn) because the while loop is inside the for loop and the while loop is also inside the while loop so the running time is O(nlogn)
        mergesort(A, q+1, r) # running time is O(nlogn) because the while loop is inside the for loop and the while loop is also inside the while loop so the running time is O(nlogn)
        merge(A, p, q, r) # running time is O(n) because it is only one loop and it is not nested inside another loop so it is O(n)



a = list(map(int, input().split()))

import time

st = time.process_time()

mergesort(a, 0, len(a)-1)

et = time.process_time()

print(a)
print(et-st)

#time complexity, iteration and explanation on how the code works 
# 1. The time complexity of this code is O(nlogn)
# 2. The iteration of this code is O(nlogn)
# 3. The iteration of this code is O(nlogn) because the while loop is inside the for loop and the while loop is also inside the while loop so the iteration is O(nlogn)

#Explanation of O(nlogn)
# 1. The mergesort function is used to sort the list of numbers in ascending order
# 2. The mergesort function is a recursive function
# 3. The mergesort function is a recursive function because it calls itself inside the function 

#When does the code become O(nlogn)?
# 1. The code becomes O(nlogn) when the list of numbers is divided into two halves because the code is using 
# divide and conquer method to sort the list of numbers in ascending order and the divide and conquer method 
# is O(nlogn) because the code is using recursion to sort the list of numbers in ascending order 

