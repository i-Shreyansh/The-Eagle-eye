from tkinter import *
import os


PATH = os.getcwd()
PATH=PATH.split("\GUI")[0]
os.chdir(PATH)
import Device as dv
dv.webcam(5)

def btn_clicked0():
    print("Button Clicked0")
    
def btn_clicked1():
    print("Button Clicked1")
    window.destroy()

window = Tk()


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
    command = btn_clicked0,
    relief = "flat")

b0.place(
    x = 211, y = 344,
    width = 207,
    height = 64)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b1.place(
    x = 8, y = 13,
    width = 112,
    height = 113)

window.resizable(False, False)
window.mainloop()
