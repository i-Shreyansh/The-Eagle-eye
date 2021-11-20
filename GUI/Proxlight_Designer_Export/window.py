from tkinter import *
import sys


def btn0_clicked():
    print("Button0 Clicked")
def btn1_clicked():
    print("Button1 Clicked")
    
def btn2_clicked():
    print("Button2 Clicked")
def btn3_clicked():
    print("Button3 Clicked")
def btn4_clicked():
    print("Button4 Clicked")
def btn5_clicked():
    print("Button5 Clicked")
def btn6_clicked():
    print("Button6 Clicked")
def btn7_clicked(): #exit
    print("Button7 Clicked")
    sys.exit()


window = Tk()

window.geometry("1000x711")
window.configure(bg = "#0b07ec")
canvas = Canvas(
    window,
    bg = "#0b07ec",
    height = 711,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.0, 355.5,
    image=background_img)


canvas.create_rectangle(
    327, 125, 327+665, 125+483,
    fill = "#c9b4e3",
    outline = "")

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn0_clicked,
    relief = "flat")

b0.place(
    x = 426, y = 4,
    width = 148,
    height = 37)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn1_clicked,
    relief = "flat")

b1.place(
    x = 232, y = 650,
    width = 207,
    height = 58)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn2_clicked,
    relief = "flat")

b2.place(
    x = 459, y = 657,
    width = 193,
    height = 51)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn3_clicked,
    relief = "flat")

b3.place(
    x = 2, y = 4,
    width = 115,
    height = 106)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn4_clicked,
    relief = "flat")

b4.place(
    x = 285, y = 3,
    width = 131,
    height = 37)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn5_clicked,
    relief = "flat")

b5.place(
    x = 144, y = 3,
    width = 131,
    height = 37)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn6_clicked,
    relief = "flat")

b6.place(
    x = 606, y = 0,
    width = 250,
    height = 53)

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn7_clicked,
    relief = "flat")

b7.place(
    x = 869, y = 3,
    width = 131,
    height = 50)

canvas.create_text(
    721.5, 26.5,
    text = "Sign up",
    fill = "#000000",
    font = ("Aclonica-Regular", int(20.0)))

canvas.create_text(
    673.0, 348.5,
    text = "Welcome to Eagle Eye",
    fill = "#000000",
    font = ("Aclonica-Regular", int(20.0)))

window.resizable(False, False)
window.mainloop()
