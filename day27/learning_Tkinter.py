from tkinter import *

window = Tk()

window.title("First tkinter program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 8, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New text"
my_label.config(text="New Text", padx=20, pady=20)

# Button
def button_click():
    my_label.config(text=input.get())

button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# input_box
input = Entry(width=15)
input.grid(column=2, row=3)
print(input.get())



window.mainloop()