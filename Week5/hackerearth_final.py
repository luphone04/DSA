table_size = int(input())
a = list(map(int, input().split()))
hash_table = [[] for i in range(table_size)]

def hash_func(key):
    return key % table_size

def insert(s, v):
    # return 0 on successful insertion
    # return -1 if s has already been in the hash table
    if search(s) != -1:
        return -1
    h = hash_func(s)
    hash_table[h].insert(0,(s,v))
    return 0

def search(s):
    # return value of the key or
    # return -1 if s does not exists in hash table
    hash_val = hash_func(s)
    for item in hash_table[hash_val]:
        if item[0] == s:
            return item[1]
    return -1

def delete(s):
    # return 0 on successful deletion
    # return -1 if s does not exists in hash table
    if search(s) == -1:
        return -1
    hash_val = hash_func(s)
    for i in range(len(hash_table[hash_val])):
        if hash_table[hash_val][i][0] == s:
            del hash_table[hash_val][i]
            return 0

for i in range(table_size):
    iKey = a[i] + (i + 1) * (i + 1)
    value = search(iKey) #search will return the total count of iKey if it exists in the array (ivalue will be count)
    if value == -1:
        insert(iKey,1) #if key isn't in the list, insert the key, with ivalue as 1 (ivalue is the count)
    else:
        # tuples are immutable
        # if the key is already in the array, we will delete the existing tuple
        # and insert the same key but with an updated ivalue since we need to add 1 to the count
        delete(iKey)
        insert(iKey, value + 1)

count = 0
for i in range(table_size):
    jKey = a[i] - (i + 1) * (i + 1)
    value = search(jKey) # we will look if there is an item that is the same as jKey in the existing array
    if value != -1: # if item that is the same as jKey is found, we will add the count of that item, value, to count
        count += value

print(count)
