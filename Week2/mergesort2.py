
def merge(A, p, q, r):
    # merge the sorted A[p:q+1] with the sorted A[q+1:r+1]
    # the result is a sorted A[p:r+1]
    # Hint: an auxiliary list is required
    # Complete the body of this function
    B = []
    i = p
    j = q+1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    A[p:r+1] = B + A[i:q+1] + A[j:r+1]
    

def mergesort(A, p, r):
    # Complete the body of this function
        #A is OG list
        #p is starting index
        #r is ending index
        #q the ending index of the first subarray 
        #  and the starting index of the second subarray.
    if p < r:
        q = (p+r)//2s
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
