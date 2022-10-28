import tkinter as tk
from PIL import ImageTk
from attr import has
from pyparsing import col

TITLE = "Dieseldog42"
GEOMETRY = "500x500"
LOGO = "src/images/logo.ico"


class Slot:
    root: tk.Tk
    column: int
    elevation: int
    elevation_row = 0
    direction: tk.PhotoImage
    direction_row = 1
    hazard: str
    hazard_row = 2
    info: str
    info_row = 3

    def __init__(self, root: tk.Tk, column: int) -> None:
        self.root = root
        self.column = column

    def update(
        self,
        elevation: int,
        direction: tk.PhotoImage,
        hazard: str = None,
        info: str = None,
    ):
        self.elevation = elevation
        self.direction = direction
        self.hazard = hazard or ""
        self.info = hazard or ""

    def refresh(self):
        pass


class DieselGUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.build_direction = dict(active={}, inactive={})
        self.load_directions()
        self.setup()
        self.active_slot = Slot(column=1)

    def setup(self):
        """
        Sets up the GUI
        Puts the window in the center of the screen
        Sets the window to always be on top
        Adds labels for the rows
        """
        self.root.title(TITLE)
        self.root.geometry(GEOMETRY)
        self.root.eval("tk::PlaceWindow . center")
        self.root.attributes("-topmost", True)
        self.root.iconbitmap(LOGO)
        elevation = tk.Label(self.root, text="Elevation 🪂")
        elevation.grid(row=0, column=0)
        direction = tk.Label(self.root, text="Direction 🗺")
        direction.grid(row=1, column=0)
        hazard = tk.Label(self.root, text="Hazard ☣")
        hazard.grid(row=2, column=0)
        info = tk.Label(self.root, text="Info 💡")
        info.grid(row=3, column=0)

    def load_directions(self):
        """
        Load the images for build directions for use in the GUI
        """
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
        """Starts the GUI"""
        self.root.mainloop()
