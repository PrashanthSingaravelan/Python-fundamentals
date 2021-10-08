from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)

## label
my_label = Label(text="Welcome all",font=("Arial",20,"bold"))
my_label.pack()

## Button
def button_click():
	print("Got clicked")
	new_text = entry_input.get()
	my_label['text'] = new_text

my_button = Button(text="Click Me",font=("Helvetica",20,"italic"),command=button_click)
my_button.pack()

## Entry
entry_input = Entry(width=30)
entry_input.pack()

window.mainloop()