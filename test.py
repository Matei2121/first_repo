
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        if b != 0:
            return a / b
        else:
            return None

print(calculator(6, 7, '+'))

