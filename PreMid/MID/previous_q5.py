x = list(map(int, input().split()))
print(len(x))

import time
dict = {}
st = time.process_time()

found = False
for i in range(len(x)):
    for j in range(i+1,len(x)):
        temp = x[i]*x[j]
        dict[temp] = dict.get(temp,())+(x[i],x[j])

        if len(dict[temp]) >= 4:
            print(f"{dict[temp][0]} {dict[temp][1]}, {dict[temp][2]} {dict[temp][3]}")
            found = True
            break        
    if found:
        break

if not found:
    print("No pair exists")

et = time.process_time()
print(et-st)
