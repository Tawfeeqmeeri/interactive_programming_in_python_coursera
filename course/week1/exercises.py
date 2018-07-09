#PRACTICE EXERCISES FOR LOGIC AND CONDITIONALS
from datetime import datetime
import math 

# Write a function that checks if number even or odd

def is_even(number):
    if number % 2 == 0:
        print(str(number)+" is an even number.")
    else:
        print(str(number)+" is an odd number.")

is_even(9)

#2 Write a function that returns True if names are either "John", "Joe" or "Stephan" and returns False otherwise

def is_cool(name):
    if name == "Tawfeeq" or "Joe" or "Stephan":
        print(str(name)+" is cool!")
    else:
        print(str(name)+" is not cool :(")

is_cool("Tawfeeq")

# Write function is_lunchtime that takes as input the parameters hour (an integer in the range [1, 12][1,12]) 
#and is_am (a Boolean “flag” that represents whether the hour is before noon).

def is_lunchtime(hour, is_am):
    return (hour == 11 and is_am) or (hours == 12 and not is_am)

def test(hour, is_am):
    #test the is_lunchtime function
    print(hour, end=" "),
    if is_am:
        print("am", end=" ")
    else: 
        print("pm", end=" ")
    if is_lunchtime(hour, is_am):
        print("is lunch time")
    else:
        print("is not lunchtime")

test(11, True)

# write a function that tells if a given year is a leap year or not

def is_leap_year(year):
    date = datetime.now().year
    if year % 4 != 0:
        if year >= date:
            print(str(year)+" is not a leap year")
        else: 
            print(str(year)+" was not a leap year")

    elif year % 100 != 0:
        if year >= date:
            print(str(year)+" is a leap year")
        else:
            print(str(year)+" was not a leap year")

    elif year % 400 != 0:
        if year >= date:
            print(str(year)+" is not a leap year")
        else:
            print(str(year)+" was not a leap year")

    else:
        if year >= date:
            print(str(year)+" is a leap year")
        else:
            print(str(year)+" was not a leap year")

is_leap_year(2000)

#write a funtion that returns name and age, but gives and error if age is less than zero.

def name_age(name, age):
    if age <= 0:
        print ("Error: Invalid age.")
    else:
        print (str(name) +" is "+str(age)+" years old")

name_age("Tawfeeq", -3)

#write a function that takes number input between 0 and 100 and prints the tens and ones digits.

def print_digits(number):
    ones = number %10
    tens = number // 10 
    print ("The tens digit is ("+str(tens)+") and the ones digit is ("+str(ones)+")")

print_digits(63)

 #same function but with user input 

def input_digits(number):
    ones = number %10
    tens = number // 10
    print ("The tens digit is (" +str(tens)+") and the ones digit is ("+str(ones)+")")

input_digits(int(input("Enter number: ")))

#write a fuction that corresponds a given first name with its last name

def name_lookup(first_name):

    if first_name =="Bruce".lower():
        return "Wayne"
    elif first_name == "Harley".lower():
        return "Quinn"
    else:
        return "Error: Name not found"

def test(first_name):
    print (name_lookup(first_name))


test(input("Enter first name: "))

# write a function that returns a given word in pig latin language

def pig_latin(word):
    vowels = ["a","e","i","o","u"]
    first_letter = word[0]
    rest_of_word = word[1:]

    if word[0] in vowels:
        print(word + "way")
    else:
        print (rest_of_word + first_letter + "ay")

pig_latin(input("Enter word: "))

# write a function that calculates the compound interest 

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    return present_value * math.pow(1+rate_per_period, periods)

print ("$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3))

# write a function that calculates the are of a regular polygon 

def area_regular_polygon(no_of_sides, length_of_each_side):
    a = math.tan(math.pi / no_of_sides)
    b = (no_of_sides) * math.pow(length_of_each_side, 2)
    c = b / a
    return c / 4

print (area_regular_polygon(5, 7))
print (area_regular_polygon(7, 3))

