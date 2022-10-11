from tkinter import *


def create_root():
    global root

    root = Tk()
    root.geometry("700x600")
    root.title("GUI Product Shop")

    return root


def create_frame():
    global frame

    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()
