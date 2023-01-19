

#Start Exercise 2
#Write a program to iterate the first ten numbers in each iteration, print the sum of the current
#and previous number

for i in range(10):

#Define current number variable as an integer in the range 0-9
  current_number = int(i);
  previous_number = current_number - 1;
  #Print Current Number and the current number variable as a string
  print("CURRENT NUMBER: " + str(current_number));
  #Print Previous Number and the previous number varialbe as a string
  print("PREVIOUS NUMBER: " + str(previous_number));
  #Print the sum of the current number and previous number, convert the sum to string to be displayed
  print("SUM: " + str((current_number) + (previous_number)));

#End Excercise 2














