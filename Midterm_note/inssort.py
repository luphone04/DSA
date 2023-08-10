import time

a = list(map(int, input().split()))

n = len(a)

st = time.process_time()

# write the insertion sort code into this segment
for i in range(1 , n): # for loop is O(n) because it is only one loop and it is not nested inside another loop so it is O(n) 
    key = a[i] # this is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1)
    j = i-1 # this is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1)
    while j >= 0 and a[j] > key: # this is O(n) because it is nested inside another loop so it is O(n)
        a[j + 1] = a[j] # this is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1) 
        j -= 1 # this is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1)
    a[j+1] = key # this is O(1) because it is only one line of code and it is not nested inside another loop so it is O(1)
et = time.process_time() 

print(a)
print(et-st)

#running time, time complexity and iteration explanation of this code
# 1. The running time of this code is O(n^2)
# 2. The time complexity of this code is O(n^2)
# 3. The iteration of this code is O(n^2)
# 4. The iteration of this code is n^2 because the while loop is inside the for loop and the while loop 
# is also inside the while loop so the iteration is n^2 
# 5. The time complexity of this code is n^2 because the while loop is inside the for loop and the while
#  loop is also inside the while loop so the time complexity is n^2

#Explnation of insertion sort code
# 1. The insertion sort code is used to sort the list of numbers in ascending order 

#When does rthe code become O(n^2)?
# 1. The code becomes O(n^2) when the while loop is inside the for loop and the while loop is also inside the 
# while loop so the iteration is n^2 
