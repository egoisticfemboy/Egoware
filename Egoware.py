import tkinter as tk
from tkinter import messagebox
import subprocess

def run_batch_file():
    batch_file = r'.\start_up.bat'  

    
    try:
        subprocess.Popen(batch_file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Batch file started successfully.")
    except Exception as e:
        print(f"Error running batch file: {e}")

def activate_main():
    subprocess.Popen(["python", "src/main.py"])

def create_files():
    subprocess.Popen(["python", "src/create_files.py"])

def main():
    root = tk.Tk()
    root.title("Activation Prompt")
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    label = tk.Label(frame, text="Are you sure you want to activate this program?", padx=10, pady=10)
    label.pack()

    btn_main = tk.Button(frame, text="Activate Main", command=activate_main, padx=10, pady=5)
    btn_main.pack(pady=5)

    btn_create = tk.Button(frame, text="Create Files", command=create_files, padx=10, pady=5)
    btn_create.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_batch_file()
    main()
