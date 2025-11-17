# Drawing Patterns with Nested Loops
#  Prompt User for Pattern Size:
size = int(input("Enter the size of the pattern: "))
# Validate that the input is positive
if size <= 0:
    print("Error: Please enter a positive integer.")
    exit()
# Initialize row counter
row = 0
# Draw the square pattern using nested loops
while row < size:
    # Print asterisks in one row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1    

