import tkinter as tk
import ctypes
import subprocess

# Definition der Konstanten für MessageBox
MB_YESNO = 4
ICON_QUESTION = 32

def main():
    root = tk.Tk()
    root.withdraw()  # Verstecke das Tkinter-Hauptfenster

    # Zeige die Ja/Nein Frage mit dem Windows-Dialog
    result = ctypes.windll.user32.MessageBoxW(0, "Are you sure you want to activate both programs?", "Activation Prompt", MB_YESNO | ICON_QUESTION)

    if result == 6:  # Wenn "Yes" ausgewählt wurde (ID 6)
        subprocess.Popen(["python", "main.py"])
        subprocess.Popen(["python", "create_files.py"])

    root.destroy()  # Schließe das Tkinter-Hauptfenster nach der MessageBox

if __name__ == "__main__":
    main()
