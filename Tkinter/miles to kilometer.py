from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300,height=300)
window.config(padx=20,pady=20)

## Input --> Miles
## Output --> Kilometers

miles_label = Label(text="Miles",font=("Arial",15,"bold"))
miles_label.grid(column=2,row=0)

kilometers_label = Label(text="Kilometers",font=("Arial",15,"bold"))
kilometers_label.grid(column=2,row=1)

equal_to = Label(text="is equal to",font=("Arial",15,"bold"))
equal_to.grid(column=0,row=1)

kilometer_result = Label(font=("Arial",23,"bold"))
kilometer_result.grid(column=1,row=1)

def button_click():
 	miles = int(input.get())
 	kilometer = float(miles*1.609)
 	kilometer_result['text'] = kilometer

input = Entry(width=7)
input.grid(column=1,row=0)

calculate_button = Button(text="Calculate",font=("Helvetica",15,"italic"),command=button_click)
calculate_button.grid(column=1,row=3)

window.mainloop()