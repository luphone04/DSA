from sys import stdin # allows you to read lines from stdin without knowing the number of lines in advance 
#stdin is a file object that is used to read data from the standard input stream, sys.stdin is a file-like object on which you can call functions read or readlines

# Read the sequence of operations to be operated on the hash table
# operations = []
# for line in stdin: 
#     line = line.split()
#     if len(line) > 2:
#         line[2] = int(line[2])
#     operations.append(line)


table_size = 10    # set table size here
hash_table = [[] for i in range(table_size)]

def show_hash_table():
    print('-------------------')
    for item_list in hash_table:
        print(item_list)
    print('-------------------')

def hash_func(s):
    char_lst = []
    value = 0
    for char in s:
        char_lst.append(char)
    for each in char_lst:
        value += ord(each)
    return value%table_size
    

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
        if hash_table[hash_val] == s:
            del hash_table[hash_val][i]

            return 0


The main program to execute the sequence of operations
for op in operations:
    # op[0] is "insert" or "search" or "delete"
    if op[0] == "insert":
        print(insert(op[1],op[2]))
        show_hash_table()
    elif op[0] == "search":
        print(search(op[1]))
    elif op[0] == "delete":
        print(delete(op[1]))
        show_hash_table()


    

