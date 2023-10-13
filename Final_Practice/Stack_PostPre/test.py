# def is_number(string):
#     try:
#         float(string)
#         return True
#     except ValueError:
#         return False


# stack = []
# postfix_expr = input().split()
# for token in postfix_expr:
#     if is_number(token):
#         stack.append(int(token))
#     else:
#         num2 = stack.pop()
#         num1 = stack.pop()
#         operation = token

#         if operation == "^":
#             operation = "**"

#         stack.append(eval(f"{num1} {operation} {num2}"))

# print('%.1f' % stack[0])



print(12//7)
print(84//14)
print(14//84)