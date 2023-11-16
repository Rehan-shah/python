from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #

def rest_timer():
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        Heading.config(fg=RED, text="long break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        Heading.config(fg=PINK, text="short break")
    else:
        count_down(WORK_MIN * 60)
        Heading.config(fg=GREEN, text="work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{int(count / 60)}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✓"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomdoro")
window.config(pady=50, padx=100, bg=YELLOW)

Heading = Label(text="Timer", font=(FONT_NAME, 45), fg=GREEN, bg=YELLOW)
Heading.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = Button(window, text="Start", highlightbackground=YELLOW, command=start_timer)
start_btn.grid(row=2, column=0)

check_label = Label(text="", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

reset_btn = Button(window, text="Reset", highlightbackground=YELLOW, command=rest_timer)
reset_btn.grid(row=2, column=2)

window.mainloop()
