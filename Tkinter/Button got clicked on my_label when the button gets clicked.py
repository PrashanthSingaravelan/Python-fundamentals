from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)

## label
my_label = Label(text="Welcome all",font=("Arial",20,"bold"))
my_label.pack()

## Button
def button_click():
	my_label['text'] = "Button got clicked"

my_button = Button(text="Click Me",font=("Helvetica",20,"italic"),command=button_click)
my_button.pack()

window.mainloop()