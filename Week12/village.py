

class heap:
    def min_compare(self, x, y):  # a default compare function for min heap
        return self.items[x].key < self.items[y].key

    def max_compare(self, x, y):  # alternative compare function
        return self.items[x].key > self.items[y].key
        
    def empty(self):
        if self.heapsize == 0:
            return True
        else:
            return False

    def heapify(self, i):
        l = i*2+1
        r = (i+1)*2
        if l < self.heapsize and self.cmp(self.a[l],self.a[i]):
            largest = l
        else:
            largest = i
        if r < self.heapsize and self.cmp(self.a[r],self.a[largest]):
            largest = r
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.items[self.a[i]].a_index = i
            self.items[self.a[largest]].a_index = largest
            self.heapify(largest)

    def extract(self):
        x = self.a[0]
        last = self.heapsize-1
        self.a[0],self.a[last] = self.a[last],self.a[0]
        self.items[self.a[0]].a_index = 0
        self.items[self.a[last]].a_index = last
        self.heapsize -= 1
        self.heapify(0)
        return x

    def buildHeap(self):
        for i in range((self.heapsize-1)//2, -1, -1):
            self.heapify(i)

    def elevate_key(self, x, new_key):   # x is an item's index, not a's index
        # There is no check for correctness here, that new_key must ONLY increase
        # prioirty of items[x]. Coder must make sure of this.
        
        self.items[x].key = new_key   # must increase priority of items[x]
        j = self.items[x].a_index
        i = (j-1)//2
        while i >= 0 and self.cmp(self.a[j], self.a[i]):  # as long as parent has less priority
            self.a[i], self.a[j] = self.a[j], self.a[i]
            self.items[self.a[i]].a_index = i
            self.items[self.a[j]].a_index = j
            j = i
            i = (j-1)//2
            
    def __init__(self, items, max_heap=False):
        self.items = items
        for i in range(len(items)):
            self.items[i].a_index = i   # a_index = item's index in the heap
        self.a = [i for i in range(len(items))]   # a is the list of item indices
        if max_heap == True:
            self.cmp = self.max_compare
        else:
            self.cmp = self.min_compare
        self.heapsize = len(self.a)
        if len(self.a) > 0:
            self.buildHeap()




#Test your program with the provided “village” test case. 
# 9 10
# 0 1 10
# 0 2 10
# 1 3 12
# 2 3 20
# 2 5 7
# 3 4 15
# 5 6 15
# 5 7 5
# 6 8 5
# 7 8 18

# Answer : 79


