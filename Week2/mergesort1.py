
def merge(A, p, q, r):
    B = []
    i = p
    j = q+1
    while i <= q and j <= r: #ensures that we continue merging elements from both sections
        #i <= q ensures that we haven't reached the end of the first section yet
        #j <= r ensures that we haven't reached the end of the second section yet
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    A[p:r+1] = B + A[i:q+1] + A[j:r+1]

def mergesort(A, p, r):
    # complete the body of this function
    if p < r:
        q = (p+r)//2
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)




a = list(map(int, input().split()))

import time

st = time.process_time()

mergesort(a, 0, len(a)-1)

et = time.process_time()

print(a)
print(et-st)
