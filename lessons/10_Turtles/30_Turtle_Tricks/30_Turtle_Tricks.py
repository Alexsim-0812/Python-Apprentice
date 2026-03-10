"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes

tina.pendown
tina.color('gray')                       # Set the color of tina to gray
tina.begin_fill()
tina.circle(70)
tina.end_fill()

tina.goto(100,30)

tina.pendown()
tina.color('red')                       # Set the color of tina to red
tina.begin_fill()
tina.circle(67)
tina.end_fill()

tina.goto(30,67)

tina.pendown()
tina.color('orange')                       # Set the color of tina to orange
tina.begin_fill()
tina.circle(41)
tina.end_fill()

tina.goto(120,60)

tina.pendown()
tina.color('purple')                       # Set the color of tina to purple
tina.begin_fill()
tina.circle(27)
tina.end_fill()
turtle.exitonclick()                    # Close the window when we click on it

# Dont forget to check in your code!