#Goal:Get the multiplication table for the given number.

#Step1:Take the integer value as input from the user.
a=input("Enter the number: ")

#Step2:Create a loop where the given value iterates until the given range is reached.
for i in range(0,11):	
  x= a*i

#Step3:print the multiplication Table  
  print a,"*",i,"=",x

