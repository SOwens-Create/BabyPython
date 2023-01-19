
from audioop import add


varset = [1, 2, 3, 4];
var = varset[1];
print(var);

print(varset[-2]);

print(varset[0:2]);


#Calculator Start

print("SELCECT AN OPTION:");
optionlist = ["1. ADD", "2. SUBTRACT", "3. MULTIPLY", "4. DIVIDE"];
print(optionlist);

operation = input();

if operation == "1":
  num1 = input("Enter first number: ");
  num2 = input("Enter second number: ");
  print("The sum is: " + str(int(num1)+ int(num2)));
elif operation == "2":
  num1 = input("Enter first number: ");
  num2 = input("Enter second number: ");
  print("The difference is: " + str(int(num1) - int(num2)));
elif operation == "3":
  num1 = input("Enter first number: ");
  num2 = input("Enter second number: ");
  print("The product is: " + str(int(num1) * int(num2)));
elif operation == "4":
  num1 = input("Enter first number: ");
  num2 = input("Enter second number: ");
  print("The solution is: " + str(int(num1) / int(num2)));
else:
  print("Invalid Input");

#End of Calculator

#Practice Exercise #1
#Calculate the multiplication and sum of two numbers
#Return their product only if the product is equal to or lower than 1000 else return their sum

print("Practice Exercise 1 Start");
num1 = input("Enter First Number: ");
num2 = input("Enter Second Number: ");

if (int(num1)*int(num2))<=1000:
  print(int(num1)*int(num2));
else:
  print(int(num1) + int(num2));

#End Exercise 1

#Start Exercise 2
#Write a program to iterate the first ten numbers in each iteration, print the sum of the current
#and previous number

for i in range(10):
  current_number = int(i);
  previous_number = current_number - 1;
  print("CURRENT NUMBER: " + str(current_number));
  print("PREVIOUS NUMBER: " + str(previous_number));
  print("SUM: " + str((current_number) + (previous_number)));

#End Excercise 2














