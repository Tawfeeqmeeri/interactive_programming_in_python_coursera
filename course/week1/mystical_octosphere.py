import random 
import time 


def number_to_fortune(number):
    # Fill in your code here.
    # Use an if...elif...else statement
    # to check each of the numbers between 0 and 7
    # and return the fortune as a string.
     if number == 0:
        return "Yes, for sure!"
     elif number == 1:
        return "Probably yes."
     elif number == 2: 
        return "Seems like yes..."
     elif number == 3:
        return "Definitely not!"
     elif number == 4:
        return "Probably not."
     elif number == 5:
        return "I really doubt it"
     elif number == 6:
        return "Not sure, check back later!"
     elif number == 7:
        return "I really can't tell"
     else:
        return "Incorrect number! Choose between 0-7"
    
# TEST SECTION...    
# Uncomment this code to test if your number_to_fortune
# helper function is working. Highlight it all
# and hit control-shift-k to uncomment it all at once.
""" number_to_fortune(0)
number_to_fortune(1)
number_to_fortune(2)
number_to_fortune(4)
number_to_fortune(5)
number_to_fortune(6)
number_to_fortune(7)
number_to_fortune(19) """

def mystical_octosphere(question):
   print ("Your question was: "+ question)
   time.sleep(3)
   print ("You shake the mystical octosphere.")
   answer_number = random.randrange(0,8)
   answer_fortune = number_to_fortune(answer_number)
   time.sleep(3)
   print ("The cloudy liquid swirls, and a reply comes into view...")
   time.sleep(3)
   print ("The mystical octosphere says..."+answer_fortune)


mystical_octosphere("Will Croatia win the World Cup 2018?")