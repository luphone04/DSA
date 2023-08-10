import time
reservationLst = [17,21,26,29,36]
reqestedTime = [8,19,24,33,40]

def verifyRequestedTime(reservationLst, reqestedTime):
    print(reqestedTime)
    found = False
    if reqestedTime < reservationLst[0]:
        print("Invalid")
    else:
        reservationLst.insert(0,reqestedTime)

        for i in range(1, len(reservationLst)):
            currentValue = reservationLst[i]
            previousIndex = i-1

            while previousIndex >= 0 and reservationLst[previousIndex] > currentValue:
                reservationLst[previousIndex+ 1] = reservationLst[previousIndex]
                previousIndex -= 1

            reservationLst[previousIndex + 1] = currentValue
            if reservationLst[-1] == reqestedTime:
                found = True
                if reservationLst[i] - reservationLst[i-1] < 3:
                    print("Invalid")
                    reservationLst.remove(reservationLst[i])    
            elif reqestedTime < reservationLst[i+1]:
                found = True
                if reservationLst[i] - reservationLst[i-1] < 3 or reservationLst[i+1] - reservationLst[i] < 3:
                    print("Invalid")
                    reservationLst.remove(reservationLst[i])
                    break    
            if found:
                break

    print(reservationLst)

st = time.process_time()
for i in reqestedTime:
    verifyRequestedTime(reservationLst, i)
et = time.process_time()
print(et-st)
