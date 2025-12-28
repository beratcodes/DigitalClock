from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("250x95")
app_window.resizable(0,0)
app_window.config(bg="Black")

text_font = ("Boulder",36,'bold')
background = "black"
foreground = "white"
border_witdh = 20

# Clock
clock_label = Label(app_window, font=("Boulder",18), bg=background, fg=foreground)
clock_label.grid(row=0,column=1,padx=10,pady=10)
# Date
date_label = Label(app_window, font=("Boulder",18), bg=background, fg=foreground)
date_label.grid(row=1,column=1,padx=10,pady=10)

def digital_clock():
    # Clock
    time_info = time.strftime("%H:%M:%S")
    clock_label.config(text=time_info)
    # Date
    date_info = time.strftime("%d %B %Y")
    date_label.config(text=date_info)
    clock_label.after(200,digital_clock)

digital_clock()
app_window.mainloop()