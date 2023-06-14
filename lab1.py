#!/usr/bin/env python3
# student - Dhruvkumar patel
#  student id number - 164386211

from datetime import datetime

def calculate_age(birth_year):
    present_year = datetime.now().year
    age = present_year - birth_year
    return age

def helloWorld():
	print(‘Hello World’)



birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
print("Your age is:", age)

try:
    birth_year = int(input("Enter your birth year: "))
    age = calculate_age(birth_year)
    print("Your age is:", age)
except ValueError:
    print("Please enter a valid birth year as an integer.")

helloWorld()
