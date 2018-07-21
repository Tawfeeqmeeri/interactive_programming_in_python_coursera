# Printing "Goodbye" with a local message variable

###################################################
# Student should enter function on the next lines.

message = "Hello"

def print_goodbye():
    message = "Goodbye"
    print (message)

###################################################
# Tests

message = "Hello"
print (message)
print_goodbye()
print (message)

message = "Ciao"
print (message)
print_goodbye()
print (message)


###################################################
# Output

#Hello
#Goodbye
#Hello
#Ciao
#Goodbye
#Ciao

# Printing "Goodbye" with a global message variable

###################################################
# Student should enter function on the next lines.

def set_goodbye():
    global message 
    message = "Goodbye"
    print (message)
###################################################
# Tests

message = "Hello"
print (message)
set_goodbye()
print (message)

message = "Ciao"
print (message)
set_goodbye()
print (message)


###################################################
# Output

#Hello
#Goodbye
#Goodbye
#Ciao
#Goodbye
#Goodbye

#3 Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
# Reset global count to zero.
# Increment global count.
# Decrement global count.
# Print global count.

count = 0

def reset():
    global count 
    count = 0

def increment():
    global count
    count += 1 

def decrement():
    global count
    count -=1 
    
def print_count():
    global count 
    print (count)

###################################################
# Test

# note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Output
#1
#2
#-2

#4 Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.

try:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
except ImportError:
    import simplegui

message = "My first frame!"

# Handler for mouse click
def click():
    print (message)

# Assign callbacks to event handlers
frame = simplegui.create_frame("My first frame", 200, 100)
frame.add_button("Click me!", click)

# Start the frame animation
frame.start()

