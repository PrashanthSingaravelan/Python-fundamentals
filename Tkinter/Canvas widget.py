from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ----------------------- UI Setup ---------------------------------#
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50)

## Inserting an image into our program

canvas = Canvas(width=200,height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.pack()

window.mainloop()