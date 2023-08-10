# Read the sequence of operations to be operated on the hash table
from sys import stdin


operations = []
for line in stdin:
    line = line.split()
    if len(line) > 2:
        line[2] = int(line[2])
    operations.append(line)



table_size = 10    # set table size here
hash_table = [[] for i in range(table_size)]

def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')

def hash_func(s):
    total = 0
    for c in s:
        total += ord(c)
    return total%table_size

def insert(s, v):
    # return 0 on successful insertion
    # return -1 if s has already been in the hash table
    if search(s) != -1:
        return -1
    else:
        h = hash_func(s)
        l = hash_table[h]
        l.append((s,v))
        return 0

def search(s):
    # return value of the key or
    # return -1 if s does not exists in hash table
    h = hash_func(s)
    l = hash_table[h]
    for item in range(len(l)):
        if l[item][0] == s:
            return l[item][0]
    return -1


def delete(s):
    # return 0 on successful deletion
    # return -1 if s does not exists in hash table
    if search(s) == -1:
        return -1
    else:
        h = hash_func(s)
        l =  hash_table[h]
        for i in range(len(l)):
            if l[i][0] == s:
                del l[i]
                break
        return 0
            



# The main program to execute the sequence of operations
# op[0] is "insert" or "search" or "delete"
for op in operations:
    if op[0] == 'insert':
        insert(op[1], op[2])
    elif op[0] == 'search':
        print(search(op[1]))
    elif op[0] == 'delete':
        delete(op[1])
    else:
        pass
show_hash_table()



    

# def hash_func(s, table_size):
#     char_lst = []
#     value = 0
#     for char in s:
#         char_lst.append(char)
#     for each in char_lst:
#         value += ord(each)
#     return value % table_size

# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.buckets = [[] for _ in range(size)]

#     def insert(self, key, value):
#         index = hash_func(key, self.size)
#         self.buckets[index].append((key, value))

#     def search(self, key):
#         index = hash_func(key, self.size)
#         for item in self.buckets[index]:
#             if item[0] == key:
#                 return item[1]
#         return -1


# def find_pairs_with_equal_products(nums):
#     n = len(nums) 
#     hash_table = HashTable(n * n)

#     for a in nums:
#         for b in nums:
#             if a == b:
#                 continue
#             product_ab = a * b
#             hash_table.insert(product_ab, (a, b))

#     for i in range(n):
#         for j in range(i + 1, n): 
#             c = nums[i]
#             d = nums[j]
#             product_cd = c * d
#             result = hash_table.search(product_cd)
#             if result != -1:
#                 return result, (c, d)

#     return None


# if __name__ == "__main__":
#     nums = list(map(int, input().split()))
#     result = find_pairs_with_equal_products(nums)

#     if result:
#         (a, b), (c, d) = result
#         print(f"{a} {b}, {c} {d}")
#     else:
#         print("No pair exists")
