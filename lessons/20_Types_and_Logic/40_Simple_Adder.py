"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.
"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

from tkinter import messagebox, simpledialog, Tk # import required modules

Firstnumber = simpledialog.askfloat(title="First number", prompt="Can you give me a number?")# Ask the user for the first number   

Secondnumber = simpledialog.askfloat(title="Second number", prompt="Can you give me another number?")# Ask the user for the second number

Sum = Firstnumber + Secondnumber

messagebox.showinfo(title="The sum of two numbers", message=Sum) #  Display the sum of the two numbers 

window.mainloop() # Keep the window open