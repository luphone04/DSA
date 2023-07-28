# 4 6 2 12 7 23 77 3
# [2, 3, 4, 6, 7, 12, 23, 77]
# 0.00011499999999999705
import time 

# a = list(map(int, input().split()))
a=  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = [10 , 9,8,7,6,5,4,3,2,1]
n = len(a)

st = time.process_time()

for i in range(1 , n):
    key = a[i]
    j = i-1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j+1] = key
et = time.process_time()

print(a)
print(et-st)
