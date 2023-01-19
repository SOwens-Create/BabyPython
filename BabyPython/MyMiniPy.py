


#Calculator Start
#Display Select an Option and list the options for the user

print("SELCECT AN OPTION:");
optionlist = ["1. ADD", "2. SUBTRACT", "3. MULTIPLY", "4. DIVIDE"];
print(optionlist);

operation = input();

#User inputs a numerical option to calculator.
#The input is a string value.

if operation == "1":

#User inputs two numbers as string values
  num1 = input("Enter first number: ");
  num2 = input("Enter second number: ");

  #Print command prints a string, the math is done using the integer values and then converted back
  #to string values to display
  print("The sum is: " + str(int(num1)+ int(num2)));

#Same code, different operation to find the difference
elif operation == "2":
  num1 = input("Enter first number: ");
  num2 = input("Enter second number: ");
  print("The difference is: " + str(int(num1) - int(num2)));

#Same code, different operation to find the product
elif operation == "3":
  num1 = input("Enter first number: ");
  num2 = input("Enter second number: ");
  print("The product is: " + str(int(num1) * int(num2)));

#Same code, different operstion to find the solution
elif operation == "4":
  num1 = input("Enter first number: ");
  num2 = input("Enter second number: ");
  print("The solution is: " + str(int(num1) / int(num2)));

#If the user inputs any number other than 1-4, display invalid input
else:
  print("Invalid Input");

#End of Calculator













