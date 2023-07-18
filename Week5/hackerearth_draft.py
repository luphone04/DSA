n = int(input())
hash_table_i = [[] for i in range(n)]
hash_table_j = [[] for i in range(n)]
a = list(map(int, input().split()))

def hash_func(num):
    return num % n

def insert_i(num):
    hi = hash_func(num)
    hash_table_i[hi].insert(0, num)

def insert_j(num):
    h = hash_func(num)
    hash_table_j[h].insert(0, num)

for i in range(n):
    insert_i(a[i] + (i+1)*(i+1))
    insert_j(a[i] - (i+1)*(i+1))

print(hash_table_i)
print(hash_table_j)

count = 0

for i in range(n):
    if len(hash_table_i[i]) > 0:
        for each_i_element in hash_table_i[i]:
            for each_j_element in hash_table_j[i]:
                if each_i_element == each_j_element:
                    count += 1

count2 = 0
for i in range(n):
    for item in hash_table_i[i]:
        if item in hash_table_j[i]:
            count2 += hash_table_i[i].count(item) * hash_table_j[i].count(item)

print(count)
print(count2)

# have tried increasing table size
# have tried checking if list is empty
# have tried checking using .in function and += counti * countj
