""" import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Hi :)"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [70, 150], 60, "Blue")

# Create a frame and assign callbacks to event handlers

frame = simplegui.create_frame("Home", 400, 200)
frame.add_button("Click here", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

 """
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

message = "Whatever.."

def click():
    global message 
    message = "In love with the caocao"

def draw(canvas):
    canvas.draw_text(message, [70, 150], 30, "yellow")

frame = simplegui.create_frame("Home", 400, 200)
frame.add_button("Click here", click)
frame.set_draw_handler(draw)

frame.start()
