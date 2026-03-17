"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

for i in range(4):
    tina.forward (100)                  # Make the turtle move as fast, but not too fast. 
    tina.left (90)

turtle.exitonclick()                    # Close the window when we click on it