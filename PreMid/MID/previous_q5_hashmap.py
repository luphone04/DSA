A = list(map(int,input().split()))
hash_table = [[] for i in range(len(A)*1000)]

def hash_func(value): 
    return value % len(hash_table)

def insert(key, v):
    hash_index = hash_func(key)
    for each in hash_table[hash_index]:
        if key == each[0]:
            return -1
    hash_table[hash_index].insert(0,(key, v))
    return 0

def search(key):
    # return value of the key or
    # return -1 if s does not exists in hash table
    hash_index = hash_func(key)
    for each in hash_table[hash_index]:
        if each[0] == key:
            return each[1]
    return -1

def delete(key):
    # return 0 on successful deletion
    # return -1 if s does not exists in hash table
    hash_index = hash_func(key)
    if search(key) == -1:
        return -1
    else:
        for each in range(0,len(hash_table[hash_index])):
            if hash_table[hash_index][each][0] == key:
                del hash_table[hash_index][each]
                return 0

import time

st = time.process_time()

for i in range(len(A)):
    for j in range(i+1, len(A)):
        temp = A[i] * A[j]
        check = search(temp)
        if check != -1:
            y = (A[i], A[j])
            x = check
            break
        insert(temp, (A[i], A[j]))
    else:
        continue
    break

else:
    y = None

et = time.process_time()
if y == None:
    print("No Pair Exists")
else:
    print(f"{y[0]} {y[1]}, {x[0]} {x[1]}")
    print(y[0] * y[1] == x[0] * x[1])
print(et-st)
    