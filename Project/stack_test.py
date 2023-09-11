
stack = []
operators = set(['+', '-', '*', '/', '^', '%'])

def PrefixToPostfix(s): #s = "--3+219"
    stack = []
    s = s[::-1]
    for i in s:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            temp = a + " " + b + " " + i
            stack.append(temp)
        else:
            #stack.append(str(i)) 
            stack.append(i)
    return stack[0]

inputs = []
while True:
    line = input() #+ 1 2    ,     - 2 2
    line = line.replace(" ", "")
    if line == '0':
        break
    inputs.append(line)   #['+12', '-22']
#print(inputs)

#print(inputs)
results = []
for input_line in inputs: #'+12'
    #print(input_line)      #+12     -22
    result = PrefixToPostfix(input_line) #ERROR START FROM HERE
    print(result)  #STRING         #ERROR SHOWING 1 2 +      1 2 +
    results.append(result) #['1 2 +', '1 2 +']
#print(results)

# for z in results: 
#     print(z)  
