import tkinter as tk
from tkinter import messagebox
import subprocess

def activate_main():
    result = messagebox.askyesno("Activation Prompt", "Are you sure you want to activate Main.py?")
    if result:
        subprocess.Popen(["python", "main.py"])

def create_files():
    result = messagebox.askyesno("Activation Prompt", "Are you sure you want to create files?")
    if result:
        subprocess.Popen(["python", "create_files.py"])

def main():
    root = tk.Tk()
    root.title("Activation Prompt")
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    label = tk.Label(frame, text="Please select an action:", padx=10, pady=10)
    label.pack()

    btn_main = tk.Button(frame, text="Activate Main.py", command=activate_main, padx=10, pady=5)
    btn_main.pack(pady=5)

    btn_create = tk.Button(frame, text="Create Files", command=create_files, padx=10, pady=5)
    btn_create.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
