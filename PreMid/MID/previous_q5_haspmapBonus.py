import time

class HashTable:

    def show_hash_table(self):
        print('-------------------')
        for item_list in self.hash_table:
            print(item_list)
        print('-------------------')


    def hash_func(self,key):
        # return the hash value
        h = key
        return h % self.table_size

    def search(self,s):
        # return value of the key or
        # return -1 if s does not exists in hash table
        h = self.hash_func(s)
        for item in self.hash_table[h]:
            if item[0] == s:
                return item[1]

        return -1


    def insert(self, s, v):
        # return 0 on successful insertion
        # return -1 if s has already been in the hash table
        if self.search(s) != -1:
            return -1

        h = self.hash_func(s)
        self.hash_table[h].insert(0, (s, v))
        return 0


    def delete(self, s):
        # return 0 on successful deletion
        # return -1 if s does not exists in hash table
        if self.search(s) == -1:
            return -1

        h = self.hash_func(s)
        theSlot = self.hash_table[h]
        for i in range(len(theSlot)):
            if theSlot[i][0] == s:
                del theSlot[i]
                return 0

    def __init__(self,table_size=1):
        self.table_size = table_size
        self.hash_table = [[] for i in range(table_size)]


nList = list(map(int, input().split()))

st = time.process_time()
Dict = HashTable(len(nList)*1000)

for i in range(len(nList)):
    for j in range(i+1,len(nList)):
        product = nList[i] * nList[j]

        if Dict.search(product) != -1:
            y = (nList[i], nList[j])
            x = Dict.search(product)
            break

        Dict.insert(product,(nList[i], nList[j]))
    else:
        continue
    break

else:
    y = None




et = time.process_time()

if not y:
    print("No Pair Exists")

else:
    print(f"{y[0]} {y[1]} , {x[0]} {x[1]}")
    print(y[0] * y[1] == x[0] * x[1])

print(et-st)