import tkinter as tk
from PIL import ImageTk
from pyparsing import col

TITLE = "Dieseldog42"
GEOMETRY = "500x500"


class DieselGUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.build_direction = dict(active={}, inactive={})
        self.load_directions()
        self.setup()

    def setup(self):
        self.root.title(TITLE)
        self.root.geometry(GEOMETRY)
        self.root.eval("tk::PlaceWindow . center")
        self.root.attributes("-topmost", True)
        self.root.iconbitmap("src/images/logo.ico")
        elevation = tk.Label(self.root, text="Elevation")
        elevation.grid(row=0, column=0)
        direction = tk.Label(self.root, text="Direction")
        direction.grid(row=1, column=0)
        hazard = tk.Label(self.root, text="Hazard")
        hazard.grid(row=2, column=0)
        info = tk.Label(self.root, text="Info")
        info.grid(row=3, column=0)

    def load_directions(self):
        self.build_direction["inactive"]["up"] = ImageTk.PhotoImage(
            file="src/images/inactive/arrow-up.png"
        )
        self.build_direction["inactive"]["right"] = ImageTk.PhotoImage(
            file="src/images/inactive/arrow-right.png"
        )
        self.build_direction["inactive"]["down"] = ImageTk.PhotoImage(
            file="src/images/inactive/arrow-down.png"
        )
        self.build_direction["inactive"]["left"] = ImageTk.PhotoImage(
            file="src/images/inactive/arrow-left.png"
        )
        self.build_direction["active"]["up"] = ImageTk.PhotoImage(
            file="src/images/active/arrow-up.png"
        )
        self.build_direction["active"]["down"] = ImageTk.PhotoImage(
            file="src/images/active/arrow-down.png"
        )
        self.build_direction["active"]["left"] = ImageTk.PhotoImage(
            file="src/images/active/arrow-left.png"
        )
        self.build_direction["active"]["right"] = ImageTk.PhotoImage(
            file="src/images/active/arrow-right.png"
        )

    def start(self):
        self.root.mainloop()
