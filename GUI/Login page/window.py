from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()
window.title("Login Page")
window.geometry("1000x500")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.0, 250.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 663, y = 450,
    width = 199,
    height = 31)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    763.5, 250.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#a7d4ff",
    highlightthickness = 0)

entry0.place(
    x = 589.5, y = 233,
    width = 348.0,
    height = 33)

canvas.create_text(
    762.5, 316.0,
    text = "Password",
    fill = "#6711d4",
    font = ("Aclonica-Regular", int(20.0)))

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    772.5, 370.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#a7d4ff",
    highlightthickness = 0)

entry1.place(
    x = 598.5, y = 353,
    width = 348.0,
    height = 33)

canvas.create_text(
    754.5, 196.0,
    text = "Ussername",
    fill = "#6711d4",
    font = ("Aclonica-Regular", int(20.0)))

window.resizable(False, False)
window.mainloop()
