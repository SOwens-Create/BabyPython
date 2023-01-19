

#Practice Exercise #1
#Calculate the multiplication and sum of two numbers
#Return their product only if the product is equal to or lower than 1000 else return their sum

print("Practice Exercise 1 Start");
num1 = input("Enter First Number: ");
num2 = input("Enter Second Number: ");

#Change the two numbers to integers and multiply
#If the product is less than or equal to 1,000 print the product
if (int(num1)*int(num2))<=1000:
  print(int(num1)*int(num2));

#If the product is greater than 1,000 print the sum
else:
  print(int(num1) + int(num2));

#End Exercise 1















