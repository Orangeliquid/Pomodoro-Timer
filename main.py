from tkinter import *
import math


class Constants:
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT_NAME = "Courier"
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20


class PomodoroTimer:
    def __init__(self, window_setup):
        self.window = window_setup
        self.reps = 0
        self.timer = None
        self.timer_label = None
        self.canvas = None
        self.tomato_img = None
        self.timer_text = None
        self.checkmarks = None
        self.start_button = None
        self.reset_button = None

    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.timer_label.config(text="Timer", bg=Constants.YELLOW, fg=Constants.GREEN, highlightthickness=0, font=(Constants.FONT_NAME, 35, "bold"))
        self.checkmarks.config(text="")
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.reps = 0

    def start_timer(self):
        self.reps += 1

        work_sec = Constants.WORK_MIN * 60
        short_break_sec = Constants.SHORT_BREAK_MIN * 60
        long_break_sec = Constants.LONG_BREAK_MIN * 60

        if self.reps % 8 == 0:
            self.count_down(long_break_sec)
            self.timer_label.config(text="Break", fg=Constants.RED, highlightthickness=0, font=(Constants.FONT_NAME, 35, "bold"))
        elif self.reps % 2 == 0:
            self.count_down(short_break_sec)
            self.timer_label.config(text="Break", fg=Constants.PINK, highlightthickness=0, font=(Constants.FONT_NAME, 35, "bold"))
        else:
            self.count_down(work_sec)
            self.timer_label.config(text="Work", fg=Constants.GREEN, highlightthickness=0, font=(Constants.FONT_NAME, 35, "bold"))

    def count_down(self, count):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            marks = ""
            work_sessions = math.floor(self.reps / 2)
            for _ in range(work_sessions):
                marks += "✔"
            self.checkmarks.config(text=marks)

    def ui_setup(self):
        self.timer_label = Label(text="Timer", bg=Constants.YELLOW, fg=Constants.GREEN, highlightthickness=0, font=(Constants.FONT_NAME, 35, "bold"))
        self.timer_label.grid(column=2, row=1)

        self.canvas = Canvas(width=200, height=224, bg=Constants.YELLOW, highlightthickness=0)
        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(Constants.FONT_NAME, 35, "bold"))
        self.canvas.grid(column=2, row=2)

        self.checkmarks = Label(bg=Constants.YELLOW, fg=Constants.GREEN, font=(Constants.FONT_NAME, 10, "bold"))
        self.checkmarks.grid(column=2, row=4)

        self.start_button = Button(text="Start", highlightthickness=0, command=self.start_timer, font=(Constants.FONT_NAME, 10, "bold"))
        self.start_button.grid(column=1, row=3)

        self.reset_button = Button(text="Reset", highlightthickness=0, command=self.reset_timer, font=(Constants.FONT_NAME, 10, "bold"))
        self.reset_button.grid(column=3, row=3)


if __name__ == "__main__":
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=Constants.YELLOW)

    pomodoro_timer = PomodoroTimer(window)
    pomodoro_timer.ui_setup()

    window.mainloop()
