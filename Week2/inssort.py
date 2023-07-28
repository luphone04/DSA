
import time

a = list(map(int, input().split()))

n = len(a)

st = time.process_time()

# write the insertion sort code into this segment
for i in range(1, n): #n=5, i=1,2,3,4
    key = a[i]  
    j = i-1
    while j >= 0 and key < a[j]: #a[j] represent the previous element
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key
et = time.process_time()

print(a)
print(et-st)

# Imagine I wish to sort the following numbers 5 3 1 6 2

# Insertion sort would first check if 3 [second value] is greater than 5 [first value]. Since this is false, the 3 would be shifted over one position to the left (swapping 5 and 3) to give 3 5 1 6 2.

# Next, the 1 would be checked against the 5 to see if the 1 is larger. Since this is false, the 1 would be shifted over (swapping the 5 and the 1) to give 3 1 5 6 2. Then the algorithm would compare the 1 again to the 3. Since the 1 is not larger, it gets shifted over again (swapping the 3 and the 1) producing 1 3 5 6 2.

# After that the algorithm checks number 6 against the 5. Since 6 is larger than 5, nothing changes. After that, the 2 is checked against the 6. Since 2 is smaller the 6 and the 2 swap. The 2 is then compared against the 5 and another swap occurs (now we have 1 3 2 5 6).

# A final swap occurs after checking the 2 against the 3 resulting in the sorted list 1 2 3 5 6. At this point, I think the algorithm would continue to (unnecessarily) compare the 2 against the 1 to make sure it's in the right position.
