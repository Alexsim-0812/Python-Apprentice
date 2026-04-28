"""A  program that controls the whole entire hotel! including room services, pool, or room upgrades!"""

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

def Move_on1():
    print("Setteing you for the browser...")

password = simpledialog.askfloat(title="First Login", prompt="Password") #password is 11020960

if password == "11020960":
   messagebox.showerror(title="Checked!" prompt="Loading on to program...")
   Move_on1
else:
    messagebox.showerror(title="Wrong password." prompt="Incorrect.")

