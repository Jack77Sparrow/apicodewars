from tkinter import *
from tkinter import ttk, messagebox
from main import plt_show, plt_one_user
from equals_languages import common_languages
root = Tk()

def button_click(inp):
    
    plt_show(inp)
    # messagebox.showinfo(title="Info", message=f"{inp}")
    print("hello world")


def button_2_click():
    inp1 = login_input.get()
    plt_one_user(inp1)


button_names = list(common_languages)
root.title("Graphic Interface")

root.geometry("500x500")
root.resizable(height=True, width=True)

canvas = Canvas(root, height=1000, width=1000)
canvas.pack()

frame = Frame(root, bg="black")
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

text = Label(frame, text="languages", bg="white", font=40, fg="black")
text.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.1, anchor="center")

login_input = Entry(frame, bg="white", fg="black")
login_input.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.05)


button_enter = Button(frame, bg="gray", fg = "white", command=button_2_click)
button_enter.place(relx=0.5, rely=0.47, relwidth=0.3, relheight=0.05, anchor="center")

# password = Entry(frame, bg="purple", show="*")
# password.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.05)

def create_buttons():
    button_width = 0.2
    button_height = 0.1
    max_columns = 3
    spacing_x = 0.05
    spacing_y = 0.05
    x_start = 0.15
    y_start = 0.5
    
    x = x_start
    y = y_start
    for i, name in enumerate(button_names):
        btn = Button(frame, text=name, bg="white", fg="black", command=lambda arg=name: button_click(arg))
        btn.place(relx=x, rely=y, relwidth=button_width, relheight=button_height)
        x += button_width + spacing_x
        if (i + 1) % max_columns == 0:
            x = x_start
            y += button_height + spacing_y


create_buttons()

root.mainloop()
