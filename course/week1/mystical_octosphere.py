import random 
import time 

# This game is based on a common toy. It is a 
# round black ball with a clear plastic window. 
# The ball is filled with murky blue liquid
# and you use it as a fortune teller. You ask 
# a yes-or-no question and shake the ball. There 
# is a white many-sided die inside with answers, 
# and when you stop shaking, one of the sides
# floats up and is readable against the window.

# Here is a sample of the kind of
# output this program should produce:

# Your question was... Will I get rich?
# You shake the mystical octosphere.
# The cloudy liquid swirls, and a reply comes into view...
# The mystical octosphere says... Probably yes.

# The possible numbers are between 0 through 7 inclusive
# (that means 0, 1, 2, 3, 4, 5, 6, or 7)
# and each number should translate to a fortune
# that would be the answer to a yes or no question.
#
# My suggested fortunes are:
# 0 - Yes, for sure!
# 1 - Probably yes.
# 2 - Seems like yes...
# 3 - Definitely not!
# 4 - Probably not.
# 5 - I really doubt it...
# 6 - Not sure, check back later!
# 7 - I really can't tell
#
# If somehow the function gets a number other than those 8
# it should send back a string saying that
# something was wrong with the input.

def number_to_fortune(number):
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
    

def mystical_octosphere(question):
   print ("Your question was: "+ question)
   time.sleep(3)
   print ("You shake the mystical octosphere.")
   answer_number = random.randrange(0,8)
   answer_fortune = number_to_fortune(answer_number)
   time.sleep(3)
   print ("The cloudy liquid swirls, and a reply comes into view...")
   time.sleep(3)
   print ("The mystical octosphere says..."+ answer_fortune)


mystical_octosphere("Will Croatia win the World Cup 2018?")