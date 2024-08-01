import tkinter as tk
from pynput import keyboard

def on_press(key):
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            return False
    except AttributeError:
        pass

def disable_close():
    pass

root = tk.Tk()
root.title("UwU")
root.geometry("2x2")

root.protocol("WM_DELETE_WINDOW", disable_close)

label = tk.Label(root, text="skill issue >:3")
label.pack(pady=20)

listener = keyboard.Listener(on_press = on_press)
listener.start()

root.mainloop