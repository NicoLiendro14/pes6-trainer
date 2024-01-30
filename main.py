import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ReadWriteMemory import ReadWriteMemory


class GameProcess:
    def __init__(self):
        self.rwm = ReadWriteMemory()
        self.process = self.rwm.get_process_by_name('PES6.exe')
        self.process.open()

    def add_goal_home(self):
        data_home_goal = self.get_home_goal()
        home_goal_value = data_home_goal['home_goal_value'] + 1
        self.process.write(data_home_goal['home_goal_pointer'], home_goal_value)

    def add_goal_away(self):
        data_away_goal = self.get_away_goal()
        away_goal_value = data_away_goal['away_goal_value'] + 1
        self.process.write(data_away_goal['away_goal_pointer'], away_goal_value)

    def get_home_goal(self):
        home_goal_pointer = self.process.get_pointer(0x1017B30)
        home_goal_value = self.process.read(home_goal_pointer)
        return {"home_goal_pointer": home_goal_pointer, "home_goal_value": home_goal_value}

    def get_away_goal(self):
        away_goal_pointer = self.process.get_pointer(0x1017E24)
        away_goal_value = self.process.read(away_goal_pointer)
        return {"away_goal_pointer": away_goal_pointer, "away_goal_value": away_goal_value}


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PES6 Trainer")
        self.root.resizable(False, False)

        pes6_icon = ImageTk.PhotoImage(Image.open("pes6_icon.png"))
        self.root.iconphoto(False, pes6_icon)

        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.game_process = GameProcess()

        self.add_goal_home_button = ttk.Button(self.frame, text="Add goal home",
                                               command=self.game_process.add_goal_home)
        self.add_goal_home_button.grid(column=0, row=0, sticky=tk.W + tk.E + tk.N + tk.S)

        self.add_goal_away_button = ttk.Button(self.frame, text="Add goal away",
                                               command=self.game_process.add_goal_away)
        self.add_goal_away_button.grid(column=0, row=1, sticky=tk.W + tk.E + tk.N + tk.S)

        self.separator = ttk.Separator(self.frame, orient="vertical")
        self.separator.grid(column=1, row=0, rowspan=2, sticky="ns", padx=10)

        self.score_label = ttk.Label(self.frame, text="")
        self.score_label.grid(column=2, row=0, rowspan=2, sticky=(tk.W, tk.E))

        self.update_scores()

    def update_scores(self):
        home_goal_value = self.game_process.get_home_goal()["home_goal_value"]
        away_goal_value = self.game_process.get_away_goal()["away_goal_value"]
        self.score_label.config(text=f"Home: {home_goal_value} - Away: {away_goal_value}")
        self.root.after(1000, self.update_scores)


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
