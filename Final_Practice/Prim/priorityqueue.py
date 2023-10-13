'''
Python 3
Each obj to be enqueued must be a class instance
A field called 'index' will be added

Two functions are required for class definition of queue's element (an object):
1) precede(self,x)
      returns True if the object precedes the object x
2) assign(self,v)
      assigns higher priority value v to the object's key
      returns True if the v is successfully assigned
      returns False if v has lower priority than object's key (not assigned)
'''


'''
Utilizing "Priority_Queue" for Prim's and Dijkstra's Algorithms:
Prim's and Dijkstra's algorithms are graph algorithms that involve finding the minimum 
spanning tree in a graph (Prim's) or finding the shortest path from a source node to all 
other nodes in a weighted graph (Dijkstra's). These algorithms often use a priority queue 
to efficiently manage the order in which nodes are processed based on their priorities 
(weights or distances).


The "elevate_key" operation is particularly valuable in such algorithms because 
it allows you to update the priority of nodes already present in the priority queue. 
his is advantageous because you can avoid enqueuing multiple copies of the same node 
with different priorities. Instead, you can directly update the priority of an existing 
node in the priority queue. This can lead to more efficient memory usage and potentially
 better runtime performance.



 Auxiliary Functions for Object Classes:
To use the "Priority_Queue" class effectively for Prim's and Dijkstra's algorithms, 
you will need to define auxiliary functions for the object class (in your case, 
the "MyClass" class) that encapsulate the specific behavior of these algorithms. 
These functions may include methods for calculating priorities (e.g., edge weights or distances) 
and updating the state of nodes.

In summary, the question is encouraging advanced students to leverage the "Priority_Queue" 
class with the "elevate_key" operation to optimize the implementation of 
Prim's and Dijkstra's algorithms. This optimization involves directly updating the
priorities of nodes in the priority queue as needed, rather than enqueuing multiple 
copies of the same nodes. To achieve this, students are expected to define additional 
methods in their object classes and use the "elevate_key" operation strategically within 
the algorithms.
'''

class Priority_Queue:
    def __init__(self):
        self.a = []
        
    def empty(self):
        if self.a == []:
            return True
        else:
            return False

    def heapify(self, i):
        l = i*2+1
        r = (i+1)*2
        if l < len(self.a) and not self.a[i].precede(self.a[l]):
            largest = l
        else:
            largest = i
        if r < len(self.a) and not self.a[largest].precede(self.a[r]):
            largest = r
        if largest != i:
            self.a[i],self.a[largest] = self.a[largest],self.a[i]
            self.a[i].index = i
            self.a[i].largest = largest
            self.heapify(largest)
        
    def enqueue(self, x):
        self.a.append(x)
        i = len(self.a)-1
        self.a[i].index = i
        j = (i-1)//2
        while i > 0 and self.a[i].precede(self.a[j]):
            self.a[i],self.a[j] = self.a[j],self.a[i]
            self.a[i].index = i
            self.a[j].index = j
            i = j
            j = (i-1)//2

    def dequeue(self):
        x = self.a[0]
        i = len(self.a)-1
        self.a[0],self.a[i] = self.a[i],self.a[0]
        self.a[0].index = 0
        self.a[i].index = i
        del self.a[i]
        self.heapify(0)
        return x

    def elevate_key(self, x, k):  # must increase priority of x
        if x.assign(k):
            i = x.index
            j = (i-1)//2
            while i > 0 and self.a[i].precede(self.a[j]):
                self.a[i],self.a[j] = self.a[j],self.a[i]
                self.a[i].index = i
                self.a[j].index = j
                i = j
                j = (i-1)//2


# Example class definition for queue's element and test code


class MyClass:
    def __init__(self, k):
        self.key = k

    def precede(self, x):
        return self.key < x.key   # do not use <= or >=

    def assign(self, v):  # v must be of higher priority value than the current key
        x = MyClass(v)  # x is a local temporary instance
        if not self.precede(x):
            self.key = v
            return True
        else:
            return False

l = []
for i in range(10):
    l.append(MyClass(100-i))

pq = Priority_Queue()
for x in l:
    pq.enqueue(x)
print(95 in (map(lambda a:a.key, pq.a)))

while not pq.empty():
    print(pq.dequeue().key)
