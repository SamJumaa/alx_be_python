# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return "Error: Division by zero" if num2 == 0 else num1 / num2
    else:
        return "Invalid operation"
