from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)

## Label widget
label = Label(text="Welcome all",font=("Arial",20,"bold"))
label.grid(column=0,row=0)  # Will appear (0,0) in the screen. The entire screen is in the format of matrix

## Button widget
def button_clicked():
	print("I got clicked")

my_button = Button(text="Click me",font=("Arial",30,"italic"),command=button_clicked)  
my_button.grid(column=1,row=1)   # How many times we click the button, that much times the message will be displayed in the output

## Entry widget
input = Entry(width=20)
input.grid(column=2,row=3)

window.mainloop()

