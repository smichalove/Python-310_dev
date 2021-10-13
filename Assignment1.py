#!/usr/bin/env python3
# Assign a string, integer and float value to variables called respectively mystring, myinteger and myfloat.
# Assignment 1 by smichalove

mystring = "string"
myinteger = 1
myfloat = 1.1
# Write code to add two int variables, storing the result in a third variable. Check that the third variable has the correct value.
varint1 = 15
varint2 = 33
varint3 = varint1+varint2

print (varint3)
#Write code to add two float variables, storing the result in a third variable. Check that the third variable has the correct value.
flt1 = 3.14
flt2 = 6.5
flt3 = flt1 + flt2

print (flt3)
#Write code to add two str variables (yes, really), storing the result in a third variable. Check that the third variable has the correct value.
strng1 = "Steven"
strng2 = "Michalove "
strng3 = strng1 + strng2

print(strng3) 
# Write code to add an int and a float variable, storing the result in a third variable. Check that the third variable has the correct value.
intflt = varint1 + flt1
print(intflt)
#Write code to add an int variable and a str variable. What happens? Why? Record your answer in a comment.
#txtint = str + strng1 #does not work as you cannot mix integers and strings in a single variable
txtint = str(varint1)+strng1 #convert the integer to a string now add

print(txtint)
''''
Try these tasks now:
Assign a string, integer and float value to variables called respectively mystring, myinteger and myfloat. Write code to prove that the values really are a str, int and float.
Can you find a way to add an int value to a str? Check the resulting value.
Multiply 5 by 7.654321 and round to 3 decimal places. Check the resulting value.
Use the input function to display a message that says “Enter your name” and places the result in a variable called myname. Check the resulting value.
Use the input function to display a message that says “Enter your favorite number” and places the result in a variable called favorite_number. Check the resulting value. And check its type. Any surprises?
Now, use input to display a message asking for a number. Then another message asking for a second number. Then print the sum of the two numbers. Check the resulting values. Any surprises? For 4 and 5 the program should display 9. If it doesn’t investigate and fix the error.
'''
rounded = round(5+7.654321,3)
print (rounded)

myname = str(input("Enter your name:"))
print("you input:",myname)

favorite_number = float(input("Enter your favorite number:"))
anothernum= float(input("Enter another number:"))
print(favorite_number+anothernum)




