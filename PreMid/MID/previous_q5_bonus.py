import time

nList = list(map(int, input().split()))

st = time.process_time()
Dict = {}

for i in range(len(nList)):
    for j in range(i+1,len(nList)):
        product = nList[i] * nList[j]

        if product in Dict:
            y = (nList[i], nList[j])
            x = Dict.get(product)
            break

        Dict[product] = (nList[i], nList[j])
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