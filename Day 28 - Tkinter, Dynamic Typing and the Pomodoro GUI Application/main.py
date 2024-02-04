import math
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
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(Cdown_timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
check_marks = ""
reps = 0

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        timer.config(text="Work",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
    elif reps % 2 == 0:
        add_check()
        count_down(SHORT_BREAK_MIN*60)
        timer.config(text="Break",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
    else:
        count_down(WORK_MIN*60)
        timer.config(text="Work",fg=RED,font=(FONT_NAME,35,"bold"),bg=YELLOW)


def add_check():
    global check_marks
    check_marks += "✔"
    check_mark.config(text=check_marks)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check_marks
    time_minute = math.floor(count / 60)
    time_seconds = count % 60

    if time_minute == 0:
        time_minute = "00"
    if time_seconds == 0:
        time_seconds = "00"
    elif time_seconds < 10:
        time_seconds = f"0{time_seconds}"
    canvas.itemconfig(create_text, text=f"{time_minute}:{time_seconds}")
    if count > 0:
        global Cdown_timer
        Cdown_timer = window.after(1000,count_down,count - 1)
    else:
        start_timer()
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer = Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
timer.grid(column=1,row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file=r"Day 28 - Tkinter, Dynamic Typing and the Pomodoro GUI Application\tomato.png")
create_image = canvas.create_image(100,112, image=photo_image)
create_text = canvas.create_text(100,130, text="00:00",fill='white',font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",command=timer_reset)
reset_button.grid(column=2,row=2)

check_mark = Label(fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)       

window.mainloop()