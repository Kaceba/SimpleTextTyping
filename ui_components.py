import tkinter as tk
import positions as position

def create_window_root(root):
    root.geometry("640x480")
    root.title("My Desktop Application")

def create_label(root):
    label = tk.Label(root, text="Hai Mari! :3")
    label.place(relx=0.5, rely=0.40, anchor="center")

def on_button_click():
    print("button clicked!")

def create_button(root):
    button = tk.Button(root, text="Click me!", command=on_button_click)
    button.place(**position.center)

def create_textbox(root):
    textbox = tk.Text(root, height=1, width=40)
    textbox.place(relx=0.5, rely=0.65, anchor="center")
    return textbox

def create_typing_label(root):
    typing_label = tk.Label(root, text="", fg="blue")
    typing_label.place(relx=0.5, rely=0.70, anchor="center")
    return typing_label
