# 4 6 2 12 7 23 77 3

import time 

a = list(map(int, input().split()))

et = time.process_time()

n = len(a)

for i in range(1, n ):
    key = a[i]
    j = i - 1
    while j >= 0 and key < a[j]:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key 


st = time.process_time()

print(a)
print(et - st)
     
          