
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame8")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("462x602")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 602,
    width = 462,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=163.0,
    y=554.0,
    width=135.71435546875,
    height=35.6824951171875
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    230.0,
    308.53619384765625,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    230.5,
    97.77801513671875,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=87.0,
    y=87.98681640625,
    width=287.0,
    height=17.5823974609375
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    230.5,
    147.98016357421875,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=87.0,
    y=138.18896484375,
    width=287.0,
    height=17.5823974609375
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    230.5,
    198.182373046875,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=87.0,
    y=188.39117431640625,
    width=287.0,
    height=17.5823974609375
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    230.5,
    248.384521484375,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=87.0,
    y=238.59332275390625,
    width=287.0,
    height=17.5823974609375
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    230.5,
    298.58673095703125,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=87.0,
    y=288.7955322265625,
    width=287.0,
    height=17.5823974609375
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    230.5,
    370.15155029296875,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=87.0,
    y=360.3603515625,
    width=287.0,
    height=17.5823974609375
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    230.5,
    420.353759765625,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=87.0,
    y=410.56256103515625,
    width=287.0,
    height=17.5823974609375
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    230.5,
    470.555908203125,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=87.0,
    y=460.76470947265625,
    width=287.0,
    height=17.5823974609375
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    230.5,
    520.7582397460938,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=87.0,
    y=510.967041015625,
    width=287.0,
    height=17.5823974609375
)

canvas.create_text(
    147.0,
    15.0,
    anchor="nw",
    text="Update Students",
    fill="#9F9F9F",
    font=("OpenSansRoman Bold", 20 * -1)
)

canvas.create_text(
    192.0,
    47.0,
    anchor="nw",
    text="Student Info",
    fill="#9F9F9F",
    font=("ArialMT", 14 * -1)
)

canvas.create_text(
    194.0,
    319.0,
    anchor="nw",
    text="Subject Info",
    fill="#9F9F9F",
    font=("ArialMT", 14 * -1)
)

canvas.create_text(
    68.0,
    66.29449462890625,
    anchor="nw",
    text="First name",
    fill="#9F9F9F",
    font=("ArialMT", 12 * -1)
)

canvas.create_text(
    68.0,
    116.4967041015625,
    anchor="nw",
    text="Last name",
    fill="#9F9F9F",
    font=("ArialMT", 12 * -1)
)

canvas.create_text(
    68.0,
    166.6988525390625,
    anchor="nw",
    text="Student ID",
    fill="#9F9F9F",
    font=("ArialMT", 12 * -1)
)

canvas.create_text(
    68.0,
    216.9010009765625,
    anchor="nw",
    text="Course",
    fill="#9F9F9F",
    font=("ArialMT", 12 * -1)
)

canvas.create_text(
    68.0,
    267.103271484375,
    anchor="nw",
    text="Section",
    fill="#9F9F9F",
    font=("ArialMT", 12 * -1)
)

canvas.create_text(
    68.0,
    338.66802978515625,
    anchor="nw",
    text="Course Code",
    fill="#9F9F9F",
    font=("ArialMT", 12 * -1)
)

canvas.create_text(
    68.0,
    388.8702392578125,
    anchor="nw",
    text="Time",
    fill="#9F9F9F",
    font=("ArialMT", 12 * -1)
)

canvas.create_text(
    68.0,
    439.0723876953125,
    anchor="nw",
    text="Day",
    fill="#9F9F9F",
    font=("ArialMT", 12 * -1)
)

canvas.create_text(
    68.0,
    489.274658203125,
    anchor="nw",
    text="Laboratory Room",
    fill="#9F9F9F",
    font=("ArialMT", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
