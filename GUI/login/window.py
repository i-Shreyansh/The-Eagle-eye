


from tkinter import *


window = Tk()
window.title("Login Page")

def btn_clicked():
    print(entry0.get())
    print(entry1.get())
    window.destroy()
    
    
window.geometry("839x500")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 839,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    424.0, 250.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 511, y = 450,
    width = 199,
    height = 31)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    611.5, 250.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#a7d4ff",
    highlightthickness = 0)

entry0.place(
    x = 437.5, y = 233,
    width = 348.0,
    height = 33)

canvas.create_text(
    610.5, 316.0,
    text = "Password",
    fill = "#6711d4",
    font = ("Aclonica-Regular", int(20.0)))

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    620.5, 370.5,
    image = entry1_img)

entry1 = Entry(
    show="*",
    bd = 0,
    bg = "#a7d4ff",
    highlightthickness = 0)

entry1.place(
    x = 446.5, y = 353,
    width = 348.0,
    height = 33)

canvas.create_text(
    602.5, 196.0,
    text = "Ussername",
    fill = "#6711d4",
    font = ("Aclonica-Regular", int(20.0)))

window.resizable(False, False)
window.mainloop()

