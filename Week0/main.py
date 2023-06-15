# n = int(input("Enter number: "))
# for i in range(1, n+1):
#     print(i, end=' ')

# Write a program that read a sequence of integers as one input, then store the numbers as integers in a Python list.
# Finally, print the list.
# Path: main.py
n = input("Enter number: ")
n = n.split()
for i in range(len(n)):
    n[i] = int(n[i])
print(n)


#3
x = " "
for z in n:
    if z % 2 != 0:
       x += str(z)+" "
x = x.split()
#change to int from str in the list
for y in range(len(x)):
    x[y] = int(x[y])
print(x)


#4
e = ""
for q in n:
    if q % 2 ==0:
        e += str(q)+" "
e = e.split()
#change to int from str in the list
for p in range(len(e)):
    e[p] = int(e[p])
e.sort()
print(e[-1])


#5
reversed_list = e[::-1]
print(reversed_list)









