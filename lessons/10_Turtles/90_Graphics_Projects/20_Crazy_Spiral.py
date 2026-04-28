"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

import turtle
import random

tina = turtle.Turtle()
tina.setup(600,600,0,0)
window = turtle.Screen()


def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def create_a_crazy_spiral():
    for i in range(67):
        tina.color(getRandomColor)
        tina.forward(67)
        tina.left(67)
        tina.forward(67)
        tina.right(67)

for i in range(67):
    create_a_crazy_spiral