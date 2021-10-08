from tkinter import * 

window = Tk()
window.title("My first GUI project")
window.minsize(width=500,height=300)

## Entry
entry = Entry(width=30)
entry.insert(END,string="Begin your task")

print(entry.get())  # Getting input from the user
entry.pack()

## Text
text = Text(height=5,width=30)   # A text box of 5 lines at that instant and 30inches broad
text.insert(END,"Multi-line Text entry")
print(text.get("1.5",END))
text.pack()

## Spin-box
def spinbox_used():
	print(spinbox.get())   # each and every time when I click the up/down arrow the output will be in python console
spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

## Scale
def scale_used(value):
	print("The scale is at : ",value)  # each and every time when I click the up/down arrow the output will be in python console
scale = Scale(from_=0,to=100,command=scale_used)
scale.pack()

## Check-button
def checkbutton_used():
	print(checked_status.get())  # If button on, prints 1 else prints 0
checked_status = IntVar()  # Simply a integer variable of checkstatus which will hold 1,if the button is clicked else 0
checkbutton = Checkbutton(text="IS on?",variable=checked_status,command=checkbutton_used)
checkbutton.pack()


## Radio-button
def radio_used():
	print("The Radio button selected : ",radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option-1",value=1,variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text="Option-2",value=2,variable=radio_state,command=radio_used)

radiobutton1.pack()
radiobutton2.pack()

## Listbox
def listbox_used():
	print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4) # Only 4 items would appear in the box at a time
fruits = ["Apple","Orange","Pineapple","Banana"]
for i in fruits:
	listbox.insert(fruits.index(i),i)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()



## Label


## Button


window.mainloop()


