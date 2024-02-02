Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Name: Emmanuel Velazquez
#Date: 1/31/24

#Problem 1: This prgram prints "Hello World"
print("Hello World")
Hello World

#Problem 2: This program greets the user with their name
user_input = input("What is your name?")
What is your name?Emmanuel
print("Hello, {user_input}!")
Hello, {user_input}!
print(f"Hello, {user_input}!")
Hello, Emmanuel!

#problem 3: This program will only greet me, and my instructor
user_name = input("What is your name?") #Gets my info
professor_name = "professor" #Gets instructors name

#Check if the user is me, or my instructor
if user_name.lower() == "Emmanuel" or user_name.lower() == professor_name.lower()
#Greet only me and professor
print(f"Hello, {user_name}.")
else: print("Sorry, I can only greet you and your professor.")
SyntaxError: multiple statements found while compiling a single statement
#Get my info
user_name = input("What is your name?")
#get my instructors name
professor_name = "professor"
#Check if its me or instructor
if user_name.lower() == "Emmanuel" or user_name.lower() == professor_name.lower()
print(f"Hello, {user_name}.")
else: print("Sorry, i can only greet you and your instrucor.")
SyntaxError: multiple statements found while compiling a single statement
# Get my info
user_name = input("What is your name?")
# Get my instructors name
professor_name = "professor"
# Check if its me or instructor
if user_name.lower() == "Emmanuel" or user_name.lower() == professor_name.lower():
    print(f"Hello, {user_name}.")
    else:
        print("sorry, I can only greet you and your instructor.")
        
SyntaxError: multiple statements found while compiling a single statement
user_name = input("what is your name?")
what is your name?Emmanuel
professor_name = "Professor"
if user_name.lower() == "Emmanuel" or user_name.lower() == professor_name.lower():
    print(f"Hello, {user_name}.")
    else:
        print("sorry, i can only greet you and your instructor.")
        
SyntaxError: invalid syntax
else:
    print("sorry, i can only greet you and your instructor.")
    
SyntaxError: invalid syntax

#problem 4: This program will compute the area of a circle
radius_str = input("Enter the radius of the circle: ")

#convert the input to a float
radius = float(radius_str)

#calc the area using the formula: area = pi* r^2
area = 3.14159 * radius**2

#display result
print(f"The area of a circle with {radius} is {area}")
SyntaxError: multiple statements found while compiling a single statement
import math
# Get the radius from the user
radius_str = input("Enter the radius of the circle: ")

#Convert the input to a float
radius = float(radius_str)

#calc the area of a circle using the formula: Area = pi *r^2
area = 3.14159 * radius ** 2

#Display the result
print(f"The area of a circle with radius {radius} is {area:.2f}")
SyntaxError: multiple statements found while compiling a single statement

#Problem 5: This program converts MPG based on miles driven and gallons used
miles_driven_str = input("enter the number of miles driven: .")
enter the number of miles driven: .60
gallons_used_str = input("enter the number of gallons used: ")
enter the number of gallons used: 3
miles_driven = float(miles_driven_str)
gallons_used = float(gallons_used_str)
mpg = miles_driven / gallons_driven
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    mpg = miles_driven / gallons_driven
NameError: name 'gallons_driven' is not defined
mpg = miles_driven / gallons_used
print(f"Your car's MPG is {mpg} miles per gallon.")
Your car's MPG is 20.0 miles per gallon.
>>> 
>>> #problem 6: This program converts fahrenheit to degrees celcius
>>> #1st get user temp in fahrenheit
>>> F_str = input("Enter the temperature in fahrenheit: ")
Enter the temperature in fahrenheit: 60
>>> 
>>> #Convernt input to float
>>> fahrenheit = float(F_str)
>>> 
>>> #Calculate temperature in Celsius
>>> celsius = (fahrenheit - 32) * 5/9
>>> 
>>> #Display the result
>>> print(f"{fehrenheit} degrees fahrenheit is equal to {celsius} degrees celsius.")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(f"{fehrenheit} degrees fahrenheit is equal to {celsius} degrees celsius.")
NameError: name 'fehrenheit' is not defined. Did you mean: 'fahrenheit'?
>>> print(f"{fahrenheit} degreen fahrenheit is equal to {celsius} degrees celsius.")
60.0 degreen fahrenheit is equal to 15.555555555555555 degrees celsius.
>>> 
>>> #problem 7: This program calculates the return day based on the length of stay
>>> # get user input for starting day number and lenght of stay
>>> start_day = int(input("enter the starting day number (0 for sunday, 1 for monday,..., 6 for saturday): "))
enter the starting day number (0 for sunday, 1 for monday,..., 6 for saturday): 5
>>> length_of_stay = int(input("Enter the length of your stay in nights: "))
Enter the length of your stay in nights: 2
>>> 
>>> #calculate the day of the week you will return
>>> return_day = (start_day + length_of_stay) % 7
>>> 
>>> #Display results
>>> print(f"If you leave on day {start_day} and stay for {length_of_stay}, you will return on day {return_day}.")
If you leave on day 5 and stay for 2, you will return on day 0.


