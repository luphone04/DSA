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

# import time

# def hash_func(s, table_size):
#     char_lst = []
#     value = 0
#     for char in s:
#         char_lst.append(char)
#     for each in char_lst:
#         value += ord(each)
#     return value % table_size

# def find_pairs_with_equal_products(nums):
#     n = len(nums)
#     hash_table = {}

#     for a in nums:
#         for b in nums:
#             if a == b:
#                 continue
#             product_ab = a * b
#             if product_ab not in hash_table:
#                 hash_table[product_ab] = (a, b)

#     for i in range(n):
#         for j in range(i + 1, n):
#             c = nums[i]
#             d = nums[j]
#             product_cd = c * d
#             if product_cd in hash_table:
#                 if c != d and c != hash_table[product_cd][0] and c != hash_table[product_cd][1]:
#                     return hash_table[product_cd], (c, d)

#     return None

# if __name__ == "__main__":
#     nums = list(map(int, input().split()))

#     start_time = time.time()
#     result = find_pairs_with_equal_products(nums)
#     end_time = time.time()

#     if result:
#         (a, b), (c, d) = result
#         print(f"{a} {b}, {c} {d}")
#     else:
#         print("No pair exists")

#     execution_time = end_time - start_time
#     print(f"Execution time: {execution_time} seconds")

