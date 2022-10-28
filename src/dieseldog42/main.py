import time
from PIL import ImageGrab, ImageOps
import pytesseract
import pyautogui as pag
from src.dieseldog42.gui import DieselGUI


# def get_coordinates() -> (int):
#     print("place cursor at top left...")
#     time.sleep(3)
#     cursor1 = pag.position()
#     print("place cursor at bottom right...")
#     time.sleep(3)
#     cursor2 = pag.position()
#     return cursor1 + cursor2


# bbox = get_coordinates()
# print(bbox)
# # bbox = (940, 35, 1150, 100)

# # bbox = (760, 0, 1150, 100)


# def take_full_screenshot():
#     ImageGrab.grab().save("./screenshot.png")


# def take_scoped_screenshot():
#     image = ImageGrab.grab(bbox=bbox)
#     image = ImageOps.invert(image)
#     image.save("./screenshot_test.png")
#     text = pytesseract.image_to_string(image=image)
#     with open("./elevation.txt", "w") as file:
#         file.write(text.rstrip())


# def print_elevation():
#     image = ImageGrab.grab(bbox=bbox)
#     image = ImageOps.invert(image)
#     text = pytesseract.image_to_string(image=image)
#     print(text.rstrip())


# for _ in range(10):
#     take_scoped_screenshot()
#     # print_elevation()
#     time.sleep(2)


gui = DieselGUI()
gui.start()
