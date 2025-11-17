#Ask the user to input a number
number = int(input("Enter a number to see its multiplication table: "))
#Generate and Print the Multiplication Table
for i in range(1,11):
    result = number * 1
 #for loop iterating from 1 to 10   
    print("{} * {} = {}".format(number,i,result))

