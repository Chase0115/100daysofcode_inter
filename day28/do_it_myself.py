from tkinter import *
import math

# ----------------------Constants------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None


# ----------------------Timer reset------------------------#
def timer_reset():
    global reps
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.after_cancel(time)
    check_maker.config(text="")


# ----------------------Timer mechanism------------------------#

def timer_start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Study", fg=GREEN)


# ----------------------CountDown mechanism------------------------#

def count_down(t):
    min = math.floor(t / 60)
    sec = t % 60
    canvas.itemconfig(timer_text, text=f"{min}:{sec:02d}")
    if t > 0:
        global time
        time = canvas.after(1000, count_down, t - 1)
    else:
        timer_start()
        mark = ""
        session = math.floor(reps / 2)
        for _ in range(session):
            mark += "V"

        check_maker.config(text=f"{mark}")


# ----------------------UI setup------------------------#
window = Tk()
window.title("Study Timer")
window.config(padx=50, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 125, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=timer_start)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=timer_reset)
reset_button.grid(column=2, row=2)

check_maker = Label(bg=YELLOW, fg=GREEN, font=("Arial", 10, "bold"), highlightthickness=0)
check_maker.grid(column=1, row=3)

window.mainloop()
