import ctypes
import time
import threading
from ctypes import WinDLL, CFUNCTYPE, POINTER, c_int, c_void_p, c_ulong, c_long


WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
VK_LWIN = 0x5B
VK_RWIN = 0x5C
LLKHF_ALTDOWN = 0x20


HookProc = CFUNCTYPE(c_long, c_int, c_ulong, POINTER(c_void_p))


user32 = WinDLL('user32', use_last_error=True)
kernel32 = WinDLL('kernel32', use_last_error=True)

SetWindowsHookEx = user32.SetWindowsHookExW
SetWindowsHookEx.restype = c_void_p
SetWindowsHookEx.argtypes = (c_int, HookProc, c_void_p, c_ulong)

UnhookWindowsHookEx = user32.UnhookWindowsHookEx
UnhookWindowsHookEx.restype = c_int
UnhookWindowsHookEx.argtypes = (c_void_p,)

CallNextHookEx = user32.CallNextHookEx
CallNextHookEx.restype = c_long
CallNextHookEx.argtypes = (c_void_p, c_int, c_ulong, POINTER(c_void_p))

GetModuleHandle = kernel32.GetModuleHandleW
GetModuleHandle.restype = c_void_p
GetModuleHandle.argtypes = (c_void_p,)


hook = None

def block_win_key(nCode, wParam, lParam):
    if nCode >= 0 and wParam == WM_KEYDOWN:
        vkCode = lParam.contents.contents.value
        if vkCode == VK_LWIN or vkCode == VK_RWIN:
            print(f"{vkCode} blocked!")
            return 1
    return CallNextHookEx(hook, nCode, wParam, lParam)

def set_hook():
    global hook
    hook_proc = HookProc(block_win_key)
    hook = SetWindowsHookEx(WH_KEYBOARD_LL, hook_proc, GetModuleHandle(None), 0)
    if not hook:
        print("Failed to install hook procedure.")
        return False
    return True

def main():
    if not set_hook():
        return

    
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

    
    UnhookWindowsHookEx(hook)

if __name__ == "__main__":
    main()

