from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)
window.config(padx=50,pady=50)   # Padding added to the overall window

label = Label(text="Welcome All",font=("Arial",20,"italic"))
label.grid(column=0,row=0)
label.config(padx=100,pady=200)

def button_click():
	print("I got clicked")
	new_text = input.get()
	label['text'] = new_text

button1 = Button(text="Click button-1",font=("Helvetica",25,"bold"),command=button_click)
button1.grid(column=2,row=2)
label.config(padx=50,pady=20)   # Padding can be applied also the individual elements also

button2 = Button(text="Click button-2",font=("Helvetica",25,"bold"),command=button_click)
button2.grid(column=3,row=0)
label.config(padx=20,pady=50)

input = Entry(width=20)
input.grid(column=4,row=3)

window.mainloop()



