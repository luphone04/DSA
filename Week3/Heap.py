'''
Python 3
A explicit comparing function is required for custom priority definition
The compare function takes two items:
  - returns True if the first item has higher priority than the second
  - returns False otherwise
The function is to be passed to the heap instantiation
'''

class heap:
    def compare(x, y):  # a default compare function for min heap
        return x < y
        
    def empty(self):
        if self.heapsize == 0:
            return True
        else:
            return False

    def heapify(self, i): #We want smaller one on the parent node indicie(the point of this function)
        l = i*2+1 #left of indicies i
        r = (i+1)*2 #right of indicies i
        if l < self.heapsize and self.cmp(self.a[l],self.a[i]): #check if l is smaller than i
            largest = l 
        else:
            largest = i
        if r < self.heapsize and self.cmp(self.a[r],self.a[largest]):#check if r is smaller than r
            largest = r
        if largest != i: #if largest is not i
            self.a[i],self.a[largest] = self.a[largest],self.a[i] #small one become "i" and og parent node become "largest"
            self.heapify(largest) #necessary to ensure that the swapped element is in its correct position within 
                                  #the subtree rooted at the largest index
        
    def insert(self, x): #The insert function serves the purpose of adding a new element to the 
                         #binary heap while maintaining the heap property.
        self.heapsize += 1  #represents the number of elements in the heap. Not the actual list
        if len(self.a) < self.heapsize: #Check if the length of the underlying list self.a is less than the updated heapsize. 
                                        #This condition checks if there is enough space 
                                        #in the list to accommodate the new element being inserted.
            self.a.append(x)      #add the new element x to the end of the list
        else:
            self.a[self.heapsize-1] = x  # Assign the new element x to the last index of the list self.a
                                        #self.heapsize-1 (which corresponds to the index of the new element)
        i = self.heapsize-1         #"i" to the index of the newly inserted element 
        j = (i-1)//2                # the index of the parent node using the formula
        while i > 0 and self.cmp(self.a[i],self.a[j]): #check if "i"(newly inserted) is smaller than j(parent node)
            self.a[i],self.a[j] = self.a[j],self.a[i] #if yes, Swap the current element with its parent 
                                     #element, as the parent is smaller in a min heap or larger in a max heap.
            i = j       # Update i to the index of the parent element.
            j = (i-1)//2   #Recalculate j to get the new parent index
                        #Then recursion happen with while loop , until either i reaches the root of the 
                        # heap (index 0) or the comparison condition fails
                        

    def extract(self): #
        x = self.a[0] #Take the first element of the list self.a (which represents the root of the heap)
                      #and assign it to the variable x. This element will eventually be returned as 
                      # the extracted value from the heap.
        last = self.heapsize-1 # Set the variable last to the index of the last element in the heap. 
                               #Since heapsize represents the number of elements in the heap, subtracting 
                               # 1 gives us the index of the last element in the list.
        self.a[0],self.a[last] = self.a[last],self.a[0] #: Swap the first element (root) with the last 
                                                     #element in the list. This step ensures that the 
                                                     # element being extracted is moved to the end of the
                                                     #  list temporarily.
        self.heapsize -= 1 # Decrease the heapsize by 1 to indicate that one element has been extracted from the heap.
        self.heapify(0) # Perform the heapify operation on the root of the heap (index 0). 
                      #This operation adjusts the heap structure and maintains the heap property by 
                      # comparing the root with its child nodes and potentially swapping elements to 
                      # satisfy the heap conditions.
        return x # Finally, return the extracted value x, which was stored from the initial root of the heap.

    def buildHeap(self):
        for i in range((self.heapsize-1)//2, -1, -1):
            self.heapify(i)

    def __init__(self, items=[], cmp=compare):
        self.a = items
        self.cmp = cmp
        self.heapsize = len(self.a)
        if len(self.a) > 0:
            self.buildHeap()



# import time 
# st = time.process_time()
# # Example class definition for heap's element and test code

# def myCompare(x, y):   # max heap
#     return x.key > y.key

# class myClass:
#     def __init__(self, k):
#         self.key = k


# testList = [i+100 for i in range(10)]

# pq1 = heap(items=testList)   # default as min heap for a list of numbers
# pq2 = heap(cmp=myCompare)  # custom class item with custom compare function

# for v in testList:
#     pq2.insert(myClass(v))

# while not pq1.empty():
#     print(pq1.extract(), end=' ')
# print()

# while not pq2.empty():
#     print(pq2.extract().key, end=' ')

# et = time.process_time()
# print("\nrunning time:", et-st)

