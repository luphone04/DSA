
# Python 3 class

class item:
    def __init__(self):
        self.p = None # parent pointer of this item in the disjoint set

x = [None]*5 # list of 5 items. [None] is a list of 1 item
for i in range(5):
    x[i] = item() # x[i] is an item
    x[i].index = i # index of this item in the list(start with 0)
    x[i].key = i+10  # key value of this item which is use for sorting purpose . 
          #The reason for i+10 is to make the key value different from the index value for sorting purpose 
          #Why adding 10 instead of 1? Because we want to see the difference between the index and the key value
for i in range(5):
    print(x[i].index, x[i].key, x[i].p)

# -------------------------------------

# Python 3 tuple

y = [] # list of tuples
for i in range(5):
    y.append((i, i*2, i*3)) # append a tuple to the list
print(y)

# -------------------------------------

# Sorting x based on the key value of each item

def itemKey(a): # a is an item
    return a.key # return the key value of the item

x.sort(key = itemKey, reverse=True) # sort x based on the key value of each item
for i in range(5):  
    print(x[i].index, x[i].key, x[i].p) # print the index, key value and parent pointer of each item in x

# -------------------------------------

# Sorting y based on the 3rd element of each tuple

def tupleKey(a): # a is a tuple 
    return a[2] # return the 3rd element of the tuple

y.sort(key = tupleKey, reverse=True) # sort y based on the 3rd element of each tuple
print(y)




