from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x711")
window.configure(bg = "#000000")
canvas = Canvas(
    window,
    bg = "#000000",
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
    343, 123, 343+640, 123+480,
    fill = "#c4c4c4",
    outline = "")

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 265, y = 630,
    width = 207,
    height = 64)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 8, y = 13,
    width = 112,
    height = 113)

window.resizable(False, False)
window.mainloop()
