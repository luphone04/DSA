
stack = []
operators = set(['+', '-', '*', '/', '^', '%'])

def PrefixToPostfix(s):
    stack = []
    s = s[::-1]
    for i in s:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            temp = a + " " + b + " " + i
            stack.append(temp)
        else:
            stack.append(i)
    return stack[0]

inputs = []
while True:
    line = input() 
    line = line.replace(" ", "")
    if line == '0':
        break
    inputs.append(line)
results = []
for input_line in inputs:
    result = PrefixToPostfix(input_line)
    print(result)  
    results.append(result)

