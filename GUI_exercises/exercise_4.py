"""
Create a graphical application in Python Tkinter that asks the user to enter two integers and
displays their sum.
"""
from tkinter import *


def callback():
    n = eval(entry_1.get())
    m = eval(entry_2.get())
    result = n + m
    label_result.configure(text='The sum is : ' + str(n) + ' + ' + str(m) + ' = ' + str(result))


root = Tk()

screen_font = ('arial', 12)

label_1 = Label(text='Enter value of integer N :', font=screen_font)
label_2 = Label(text='Enter value of integer M :', font=screen_font)

label_result = Label(font=screen_font)

entry_1 = Entry(font=screen_font, width=20)
entry_2 = Entry(font=screen_font, width=20)
button_validate = Button(text='Validate', font=screen_font, width=20, command=callback)

# Let's grid out widgets
label_1.grid(row=0, column=0, padx=10, pady=10)
label_2.grid(row=1, column=0, padx=10, pady=10)
entry_1.grid(row=0, column=1, padx=10, pady=10)
entry_2.grid(row=1, column=1, padx=10, pady=10)
label_result.grid(row=2, column=1)
button_validate.grid(row=3, column=1, padx=10, pady=10)

mainloop()
