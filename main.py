import tkinter as tk
import ui_components as ui

def main():
    root = tk.Tk()
    create_window(root)
    root.mainloop()

def create_window(root):
    ui.create_window_root(root)
    ui.create_label(root)
    ui.create_button(root)

#You only really care about this stuff and below (line 15 to 31)
    textbox = ui.create_textbox(root)
    typing_label = ui.create_typing_label(root)

    # Bind the updating_content function to the textbox
    def updating_content():
        content = textbox.get("1.0", tk.END).strip()
        if content:
            typing_label.config(text="mar is typing...")
        else:
            typing_label.config(text="")

    def on_text_modified(event):
        event.widget.edit_modified(False)
        updating_content()

    # Bind to <<Modified>> event
    textbox.bind('<<Modified>>', on_text_modified)

if __name__ == "__main__":
    main()