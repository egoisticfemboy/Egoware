import ctypes
import ctypes.wintypes
import threading

WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
WM_SYSKEYDOWN = 0x0104
VK_MENU = 0x12

LowLevelKeyboardProc = ctypes.WINFUNCTYPE(
    ctypes.c_long,
    ctypes.c_int,
    ctypes.wparam,
    ctypes.lparam
)

hhkLowLevelKybd = None

def install_hook_proc():
    global hhkLowLevelKybd
    hhkLowLevelKybd = ctypes.windll.user32.SetWindowsHookExW(
        WH_KEYBOARD_LL,
        LowLevelKeyboardProc(hook_proc),
        0,
        0
    )
    if not hhkLowLevelKybd:
        print("FAILED TO INSTALL HOOK")
        return False
    return True

def hook_proc(nCode, wParam, lParam):
    if nCode == 0:
        kbdllhookstruct = ctypes.cast(lParam, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
        if wParam == WM_KEYDOWN or wParam == WM_KEYDOWN:
            if kbdllhookstruct.vkCode == VK_MENU:
                return 1
    return ctypes.windll.user32.CallNextHookEx(hhkLowLevelKybd, nCode, wParam, lParam)

class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("vkCode", ctypes.wintypes.DWORD),
        ("scanCode", ctypes.wintypes.DWORD),
        ("flags", ctypes.wintypes.DWORD),
        ("time", ctypes.wintypes.DWORD),
        ("dwExtraInfo", ctypes.wintypes.ULONG)
    ]

def message_loop():
    msg = ctypes.wintypes.MSG()
    while ctypes.windll.user32.GetMessageW(ctypes.byref(msg), 0, 0, 0) != 0:
        ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
        ctypes.windll.user32.DispatchMessageW(ctypes.byref(msg))

if __name__ == "__main__":
    if install_hook_proc():
        print("Alt key blocker is running. Press Ctrl+C to quit.")
        try:
            message_loop()
        except KeyboardInterrupt:
            pass