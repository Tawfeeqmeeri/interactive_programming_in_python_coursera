import math
import random
from random import randint

#write a function that returns number of feet in miles
def miles_to_feet(miles):
    miles_to_feet = miles * 5280
    return miles_to_feet

print (miles_to_feet(2))

#write a function that returns the total number of seconds
def total_seconds(hours, minutes, seconds):
    hrs = hours*3600
    min = minutes *60
    sec = seconds * 1
    total_seconds = hrs + min + sec 
    return (str(hours)+" hours, "+str(minutes) +" minutes and "+str(sec)+" seconds equal to "+ str(total_seconds)+" seconds.")


print(total_seconds(5, 2, 100))

#write a functions that returns the parametes of a rectangle in inches
def rectangle_area(height, width):
    rectangle_area = height * width 
    return "The area of the rectangle is " + str(rectangle_area)


print(rectangle_area(12,12))

#write a function that returns the circumference of a circle 

def circle_circumference(radius):
    circle_circumference = math.pi * radius*2
    return "The circumference of circle has " + str(circle_circumference) + " inches."

print(circle_circumference(10))

#write a functio  that returns the area of a circle

def cricle_area(radius):
    cricle_area=math.pi*radius**2
    return "The area of a circle is " + str(cricle_area)+ " square inches." 

print(cricle_area(10))

#write a function that returns the future value of the present value
def future_value(present_value, annual_rate, years):
    future_value = present_value * (1+0.01*annual_rate) ** years 
    return "The future value of $"+ str(present_value) + " with the annual rate of "+ str(annual_rate) +" for "+str(years)+" years is " + str(future_value)

print(future_value(1000, 7, 10)) 

#write a function that takes as input the parameters first_name and last_name(strings) and returns a string of the form "My name is % %"
def name_tag(first_name, last_name):
    return "My name is "+first_name+" "+last_name
    print(name_tag(first_name, last_name))
    


def test(first_name, last_name):
    print(name_tag(first_name, last_name))

test("Tawfeeq", "Meeri")


#write a function that returns name and hobby

def name_hobby(first_name, last_name, hobby):
    print(name_tag(first_name, last_name)+" and I am a " + hobby)

name_hobby("Tawfeeq", "Meeri", "sketch artist")

#write a function that reurns distance between 2 points

def point_distance(x0, y0, x1, y1):
    return math.sqrt((x0 - x1) ** 2 + (y0 - y1)  ** 2) 
  

print(point_distance(2,2,5,6))
print(point_distance(1,1,2,2))
print(point_distance(0,0,3,4)) 

def triangle_area(x0,y0,x1,y1,x2,y2):
    a=point_distance(x0,y0,x1,y1)
    b=point_distance(x0,y0,x2,y2)
    c=point_distance(x1,y1,x2,y2)
    s=(a+b+c) / 2
    return (s*(s-a)*(s-b)*(s-c))**0.5


def test(x0, y0, x1, y1, x2, y2):
    print (triangle_area(x0, y0, x1, y1, x2, y2)) 

test(0, 0, 3, 4, 1, 1)
test(-2, 4, 1, 6, 2, 1)
test(10, 0, 0, 0, 0, 10)

#write a function that breaks down number into tens and ones
def print_digits(number):
   print("The tens digit is "+str(number//10)+", and the ones is "+str(number%10)+".")

print_digits(42)

#write a definition that imitates the powerball game

def powerball():
    print("Today's numbers are " + str(random.randint(1, 60))+"و "
    +str(random.randint(1,60))+"و "+str(random.randint(1,60))+", "
    +str(random.randint(1,60))+"و "+str(random.randint(1,60))+" and the powerball number is "
    +str(random.randint(1,60)))

powerball()

# computes the area of a triangle
def triangle_area(base, height):     # header - ends in colon
    area = (1.0 / 2) * base * height # body - all of body is indented
    return area                      # body - return outputs value

a1 = triangle_area(3, 8)
print (a1)
a2 = triangle_area(14, 2)
print (a2)

# converts fahrenheit to celsius
def fahrenheit2celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius

# test
c1 = fahrenheit2celsius(32)
c2 = fahrenheit2celsius(212)
print (c1, c2)

# converts fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

# test
k1 = fahrenheit2kelvin(32)
k2 = fahrenheit2kelvin(212)
print (k1, k2)

# prints hello, world!
def hello():
    print ("Hello, world!")

# test
hello()      # call to hello prints "Hello, world!"
h = hello()  # call to hello prints "Hello, world!" a second time
print (h)      # prints None since there was no return value


class Employee: 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Tawfeeq', 'Meeri', 5000)
emp_2 = Employee('Balzadar', "Homadro", 3000)
print("Mr. "+emp_1.last+" gets paid "+ str(emp_1.pay) +" Euros")

