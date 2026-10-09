# Postfix Expression Evaluation using Stack

def evaluate_postfix(expression):
    stack = []

    for ch in expression:

        # If number, push into stack
        if ch.isdigit():
            stack.append(int(ch))

        # If operator, perform operation
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)

    return stack.pop()


# Main program
expression = input("Enter postfix expression: ")

result = evaluate_postfix(expression)

print("Result:", result)