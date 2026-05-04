"""
Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help
"""

import turtle 
import random                          # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


forwards = [ 100,110,120,130,140,150,160,170 ]
lefts = [ 30,40,50,60,70,80,90,100 ]

def startdrawing():
    tina.color(getRandomColor)
    tina.forward(forwards)
    tina.left(lefts)

for i in range(27):
    startdrawing

turtle.exitonclick()  