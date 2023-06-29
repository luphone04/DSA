
import time 
st = time.process_time()



def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j]: #less than list_a[min_value]: #"angled brackets not allowed in youtube description"
                min_value = j


        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a



print(selection_sort([7,8,9,8,7,6,5,6,7,8,9,0]))
et = time.process_time()
print("running time:", et-st)
