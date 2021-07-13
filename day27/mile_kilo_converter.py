from tkinter import *

FONT = ("Arial", 13)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=160)
window.config(padx=20, pady=30)

# Input box
input = Entry(width=10)
input.grid(column=1, row=0)

# Label Mile, is equal to, result, Km
mile = Label(text="Miles", font=FONT)
mile.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)

result = Label(text=0, font=FONT)
result.grid(column=1, row=1)

kilometer = Label(text="Km", font=FONT)
kilometer.grid(column=2, row=1)


# Button "Calculate"
def button_function():
    result.config(text=format(float(input.get()) * 1.609, '.2f'))


button = Button(text="Calculate", font=FONT, command=button_function)
button.grid(column=1, row=2)

window.mainloop()
