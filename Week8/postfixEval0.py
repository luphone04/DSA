
def is_number(string): 
    try:
        float(string)
        return True
    except ValueError:
        return False

Stack = []
postfix_expr = input().split() # Read input postfix expression as a list of tokens separated by spaces
for token in postfix_expr:
    if is_number(token): #check if token is a number or an operator 
        # Fill in code here for token being a number
        Stack.append(float(token)) # Push the number onto the stack
    else:
        # Fill in code here for token being an operator
        if token == '+':
            Stack.append(Stack.pop() + Stack.pop()) #pop take the last element of the list
        elif token == '-':
            op2 = Stack.pop()
            Stack.append(Stack.pop() - op2)
        elif token == '*':
            Stack.append(Stack.pop() * Stack.pop())
        elif token == '/':
            op2 = Stack.pop()
            if op2 != 0.0:
                Stack.append(Stack.pop() / op2)
            else:
                raise ValueError("division by zero found!")
        elif token == '^':
            Stack.append(Stack.pop() ** Stack.pop())
        elif token == '%':
            op2 = Stack.pop()
            if op2 != 0.0:
                Stack.append(Stack.pop() % op2)
            else:
                raise ValueError("division by zero found!")
        else:

            raise ValueError("unknown token {0}".format(token))
        
print('%.1f' % Stack[0])


        
