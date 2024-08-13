# Description: A GUI program that will delete any text typed into a text box if the user stops typing for 5 seconds.

# Import the tkinter module
from tkinter import *

# Timer control variables
seconds = 5
timer_running = False

# Function to clear the text box
def clear_text():
    text_box.delete(1.0, END)

# Function to count down the timer
def countdown():
    global timer_running
    if timer_running:
        window.after(1000, countdown)
        global seconds
        seconds -= 1
        if seconds == 0:
            clear_text()
            seconds = 5
            timer_running = False

# Function to start the timer
def start_timer(event):
    global timer_running
    if not timer_running:
        timer_running = True
        countdown()

# Function to reset the timer
def reset_timer(event):
    global seconds
    seconds = 5

# Create the main window
window = Tk()
window.title("Disappearing Text App")
window.minsize(width=500, height=300)

# Title label
title = Label(window, text="Don't Stop Typing!", font=("Arial", 24))
title.pack()

# Text entry box
text_box = Text(window, height=10, width=50)
text_box.pack()

# Bind the start_timer function to the text box
text_box.bind("<KeyRelease>", start_timer)
text_box.bind("<KeyPress>", reset_timer)

window.mainloop()
