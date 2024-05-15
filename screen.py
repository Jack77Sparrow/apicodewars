from tkinter import *
from tkinter import ttk, messagebox
from main import plt_show
from equals_languages import common_languages
root = Tk()

def button_click(inp):
    
    plt_show(inp)
    # messagebox.showinfo(title="Info", message=f"{inp}")
    print("hello world")


button_names = list(common_languages)
root.title("Graphic Interface")

root.geometry("500x500")
root.resizable(height=True, width=True)

canvas = Canvas(root, height=1000, width=1000)
canvas.pack()

frame = Frame(root, bg="blue")
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

text = Label(frame, text="Python", bg="red", font=40)
text.place(relx=0.20, rely=0.20, relwidth=0.3, relheight=0.1)

login_input = Entry(frame, bg="purple")
login_input.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.05)

password = Entry(frame, bg="purple", show="*")
password.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.05)

def create_buttons():
    button_width = 0.2
    button_height = 0.1
    spacing_x = 0.1
    spacing_y = 0.15
    x = 0.1
    y = 0.6
    for i in range(len(button_names)):
        btn = Button(frame, text=f"{button_names[i]}", bg="white", fg="black", command=lambda arg=button_names[i]: button_click(arg))
        btn.place(relx=x, rely=y, relwidth=button_width, relheight=button_height)
        x += button_width + spacing_x
        if i % 5 == 0:
            x = 0.1
            y += button_height + spacing_y

create_buttons()

root.mainloop()
