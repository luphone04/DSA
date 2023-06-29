# 4 6 2 12 7 23 77 3
# [2, 4, 6, 12, 3, 7, 23, 77]
# 9.60000000000058e-05


def merge(A , p , q, r):
    B = []
    i = p
    j = q + 1
    while i <= p and j <= r:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    A[p : r + 1] = B + A[i : q + 1] + A[j : r + 1]


def mergesort(A , p , r):
    if p < r: 
        q = (p + r)//2
        mergesort(A , p , q)
        mergesort(A , q + 1 , r)
        merge(A , p , q , r)

a = list(map(int , input().split()))
import time
st = time.process_time()
mergesort(a , 0 , len(a)-1)
et = time.process_time()
print(a)
print(et - st)