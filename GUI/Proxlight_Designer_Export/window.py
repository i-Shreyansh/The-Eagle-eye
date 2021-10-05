from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()
window.title("Home")

window.geometry("1200x620")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 620,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    600.5, 313.0,
    image=background_img)


canvas.create_rectangle(
    561, 70, 561+640, 70+480,
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
    x = 211, y = 344,
    width = 207,
    height = 64)

window.resizable(False, False)
window.mainloop()
