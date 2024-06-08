opr = ['+', '-', '*', '/']
def calc(num1, num2, opr):
    if opr == '+':
        result = num1 + num2
    
    if opr == '-':
        result = num1 - num2
    
    if opr == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error! Division by zero."
        
    if opr == '*':
        result = num1 * num2
        
    return result