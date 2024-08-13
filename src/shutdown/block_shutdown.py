import ctypes
from ctypes import wintypes
import win32api
import win32gui
import win32con

# REMINDER! THIS IS JUST AN EASY WAY HOW TO CODE AN SHUTDOWN BLOCKER BUT THERE ARE WAY 
# BETTER OPTIONS AND WAY MORE COMPLICATED! I RECOMMEND TO MAKE IT BETTER IF YOU WANT 
# TO USE IT FOR SOMETHING DIFFEREN BUT REMEMBER, IF YOU HARM ANYONE I AM NOT LIABLE FOR ANYTHING!


def WindowProc(hwnd, uMsg, wParam, lParam):
    if uMsg == win32con.WM_QUERYENDSESSION:
       
        return 0  
    elif uMsg == win32con.WM_DESTROY:
        win32api.PostQuitMessage(0)
        return 0
    else:
        return win32gui.DefWindowProc(hwnd, uMsg, wParam, lParam)


class_name = "BlockShutdownWindowClass"

wnd_class = win32gui.WNDCLASS()
wnd_class.lpfnWndProc = WindowProc
wnd_class.hInstance = win32api.GetModuleHandle(None)
wnd_class.lpszClassName = class_name

win32gui.RegisterClass(wnd_class)


hwnd = win32gui.CreateWindowEx(
    0,                             
    class_name,                    
    "Block Shutdown",            
    0,                            
    win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,  
    win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,   
    0,                            
    0,                             
    win32api.GetModuleHandle(None), 
    None                           
)

if hwnd == 0:
    raise Exception("Failed to create window")


msg = wintypes.MSG()
while win32gui.GetMessage(msg, 0, 0, 0):
    win32gui.TranslateMessage(msg)
    win32gui.DispatchMessage(msg)
