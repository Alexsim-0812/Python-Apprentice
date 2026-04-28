"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().
"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

Firstnumber = simpledialog.askfloat(title="First number", prompt="Can you give me a number?")# Ask the user for the first number   

Secondnumber = simpledialog.askfloat(title="Second number", prompt="Can you give me another number?")# Ask the user for the second number

Opration = simpledialog.askfloat(title="Second number", prompt="Should I add? subtract? multiply? or devide?")

if Opration == "add":
   answer = Firstnumber + Secondnumber
elif Opration == "subtract":
   answer = Firstnumber - Secondnumber
elif Opration == "multiply":
   answer = Firstnumber * Secondnumber
elif Opration == "devide":
   answer = Firstnumber / Secondnumber
else:
   messagebox.showerror(title="Unknown input" prompt="Please write the opration again.")

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open