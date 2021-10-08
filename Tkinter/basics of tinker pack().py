import tkinter
# from tkinter import * 
# Import all the tkinter module, so as not to mention the obj.class() again and again
# Eg --> tkinter.Label()  can be simply Label()
# Eg --> tkinter.Button() can be simply Button()

window = tkinter.Tk()
window.title("My first GUI program") # Gives the title to the window that too in the title bar
window.minsize(width=500,height=300) # Sizing the window 

## Label
my_label = tkinter.Label(text="Its me Prashanth.S",font=("Helvetica",24,"bold"))  # Label is defined 
my_label.pack() # Generally, the label appears in the center of the screen

# my_label.pack(side="left")  Alligns to the left end of the screen

# To change the text content in my_label
# 1) my_label['text'] = "New Text"
# 2) my_label.config(text="New Text")

## Button
def button_clicked():
	print("I got clicked")

my_button = tkinter.Button(text="Click me",font=("Arial",30,"italic"),command=button_clicked)  # command = function name and not function call
my_button.pack()   # How many times we click the button, that much times the message will be displayed in the output

## Entry 
input = tkinter.Entry(width=20)
input.pack()

window.mainloop()



