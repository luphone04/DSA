testList = [i+100 for i in range(10)] 
import time

class heap:
    def compare(x, y):  # a default compare function for min heap
        return x < y

    def empty(self):
        if self.heapsize == 0:
            return True
        else:
            return False

    def heapify(self, i):
        l = i * 2 + 1
        r = (i + 1) * 2
        if l < self.heapsize and self.cmp(self.a[l], self.a[i]):
            largest = l
        else:
            largest = i
        if r < self.heapsize and self.cmp(self.a[r], self.a[largest]):
            largest = r
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.heapify(largest)

    def insert(self, x):
        self.heapsize += 1
        if len(self.a) < self.heapsize:
            self.a.append(x)
        else:
            self.a[self.heapsize - 1] = x
        i = self.heapsize - 1
        j = (i - 1) // 2
        while i > 0 and self.cmp(self.a[i], self.a[j]):
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j
            j = (i - 1) // 2

    def extract(self):
        x = self.a[0]
        last = self.heapsize - 1
        self.a[0], self.a[last] = self.a[last], self.a[0]
        self.heapsize -= 1
        self.heapify(0)
        return x

    def buildHeap(self):
        for i in range((self.heapsize - 1) // 2, -1, -1):
            self.heapify(i)

    def __init__(self, items=[], cmp=compare):
        self.a = items
        self.cmp = cmp
        self.heapsize = len(self.a)
        if len(self.a) > 0:
            self.buildHeap()

def getRopeMinCost(costs):

    pq1 = heap(costs)
    cost = 0

    while pq1.heapsize > 1:
        x = pq1.extract()
        y = pq1.extract()
        total = x + y
        pq1.insert(total)
        cost += total
    return cost

st = time.process_time()
arr = list(map(int, input().split()))
print(getRopeMinCost(arr))
et = time.process_time()
print(et-st)


#100ropes.in
# 340236
# 0.0009559999999999985


#1000ropes.in
# 4759002
# 0.013037

#2000ropes.in
# 10806430
# 0.028231000000000006

#4000ropes.in
# 23531868
# 0.062099

#8000ropes.in
# 50620561
# 0.14127

#16000ropes.in
# 109583364
# 0.30248200000000003

#32000ropes.in
# 236759760
# 0.6565510000000001