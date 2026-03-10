"""
For this program, you will tell Tina the Turtle to draw a triangle.

You should look at the previous programs to see how to use the turtle commands.
Copy lines of code from those programs to this one to draw a triangle.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

tina.penup()#put pen up
tina.goto(-100,90)#makes tina go to -100,90
tina.pendown()#put pen down

tina.forward(100)#makes tina move 100 steps
tina.left(120)#makes tina turn 60 degress

tina.forward(100)#makes tina move 100 steps
tina.left(120)#makes tina turn 60 degress

tina.forward(100)#makes tina move 100 steps
tina.left(120)#makes tina turn 60 degress


turtle.exitonclick()                    # Close the window when we click on it