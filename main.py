import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()
process = rwm.get_process_by_name('notepad.exe')
process.open()


def add_goal_home():
    data_home_goal = get_home_goal()
    home_goal_value = data_home_goal['home_goal_value'] + 1
    process.write(data_home_goal['home_goal_pointer'], home_goal_value)


def add_goal_away():
    data_away_goal = get_away_goal()
    away_goal_value = data_away_goal['away_goal_value'] + 1
    process.write(data_away_goal['away_goal_pointer'], away_goal_value)


def get_home_goal():
    home_goal_pointer = process.get_pointer(0x1017B30)
    home_goal_value = process.read(home_goal_pointer)
    return {"home_goal_pointer": home_goal_pointer, "home_goal_value": home_goal_value}


def get_away_goal():
    away_goal_pointer = process.get_pointer(0x1017E24)
    away_goal_value = process.read(away_goal_pointer)
    return {"away_goal_pointer": away_goal_pointer, "away_goal_value": away_goal_value}


root = tk.Tk()
root.title("PES6 Trainer")

pes6_icon = ImageTk.PhotoImage(Image.open("pes6_icon.png"))
root.iconphoto(False, pes6_icon)

root.resizable(False, False)

frame = ttk.Frame(root, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

add_goal_home_button = ttk.Button(frame, text="Add goal home", command=add_goal_home)
add_goal_home_button.grid(column=0, row=0, sticky=tk.W + tk.E + tk.N + tk.S)

add_goal_away_button = ttk.Button(frame, text="Add goal away", command=add_goal_away)
add_goal_away_button.grid(column=0, row=1, sticky=tk.W + tk.E + tk.N + tk.S)

separator = ttk.Separator(frame, orient="vertical")
separator.grid(column=1, row=0, rowspan=2, sticky="ns", padx=10)


def update_scores():
    home_goal_value = get_home_goal()["home_goal_value"]
    away_goal_value = get_away_goal()["away_goal_value"]
    score_label.config(text=f"Home: {home_goal_value} - Away: {away_goal_value}")
    root.after(1000, update_scores)


score_label = ttk.Label(frame, text="")
score_label.grid(column=2, row=0, rowspan=2, sticky=(tk.W, tk.E))

update_scores()

root.mainloop()
