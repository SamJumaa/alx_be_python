#  Simple Calculator
#ask the use to enter wo numbers each after the other
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#Ask for the type of operation to performe
operation=input("Choose the operation (+, -, *, /): ")
# Initialize result
result = None
#Perform the Calculation Using match-case
match operation:
    case "+":
        result = num1 + num2   
    case "-": 
        result = num1-num2   
    case "*":
        result = num1 * num2  
    case "/": 
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")  
# Print result if calculation was successful
if result is not None:
    # Round the result to 2 decimal places
    print("The result is {}".format(round(result, 2)))  