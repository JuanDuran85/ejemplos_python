from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Clock")
app_window.geometry("410x140")
app_window.resizable(1, 1)

text_font = ("Arial", 68, "bold")
background_color = "#f2e750"
foreground_color = "#663529"
border_width = 30

label = Label(app_window, font=text_font, bg=background_color, fg=foreground_color, bd=border_width)
label.grid(row=8, column=1)

def digital_clock():
    time_line = time.strftime("%H:%M:%S")
    label.config(text=time_line)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()