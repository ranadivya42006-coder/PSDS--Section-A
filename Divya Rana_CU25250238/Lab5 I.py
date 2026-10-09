# Infix to Postfix conversion using Stack

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for ch in expression:

        # If operand, add to postfix
        if ch.isalnum():
            postfix += ch

        # If '(', push into stack
        elif ch == '(':
            stack.append(ch)

        # If ')', pop until '('
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        # If operator
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                postfix += stack.pop()
            stack.append(ch)

    # Pop remaining operators
    while stack:
        postfix += stack.pop()

    return postfix


# Main program
expression = input("Enter infix expression: ")

result = infix_to_postfix(expression)

print("Postfix expression:", result)