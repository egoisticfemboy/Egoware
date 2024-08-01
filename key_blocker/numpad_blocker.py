import ctypes
import threading
import win32service
import win32serviceutil
import win32api
import win32event
import win32con
import win32gui

SERVICE_NAME = 'NumpadBlockerService'

class NumpadBlockerService(win32serviceutil.ServiceFramework):
    _svc_name_ = SERVICE_NAME
    _svc_display_name_ = 'Numpad Blocker Service'
    _svc_description_ = 'Blocks numpad keys.'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.stop_event = threading.Event()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.stop_event.set()
    
    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        self.stop_event.clear()

        
        self.hook_id = None
        def low_level_keyboard_proc(nCode, wParam, lParam):
            if nCode == win32con.HC_ACTION:
                keyboard_struct = ctypes.cast(lParam, ctypes.POINTER(ctypes.c_ulong * 6)).contents
                vkCode = keyboard_struct[0]
                if vkCode in [win32con.VK_NUMPAD0, win32con.VK_NUMPAD1, win32con.VK_NUMPAD2, win32con.VK_NUMPAD3,
                              win32con.VK_NUMPAD4, win32con.VK_NUMPAD5, win32con.VK_NUMPAD6, win32con.VK_NUMPAD7,
                              win32con.VK_NUMPAD8, win32con.VK_NUMPAD9, win32con.VK_DECIMAL, win32con.VK_DIVIDE,
                              win32con.VK_MULTIPLY, win32con.VK_SUBTRACT, win32con.VK_ADD]:
                    return 1
            return win32api.CallNextHookEx(self.hook_id, nCode, wParam, lParam)

        LowLevelKeyboardProcType = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, ctypes.wparam, ctypes.lparam)
        self.hook_id = ctypes.windll.user32.SetWindowsHookExA(win32con.WH_KEYBOARD_LL,
                                                              LowLevelKeyboardProcType(low_level_keyboard_proc),
                                                              win32api.GetModuleHandle(None), 0)
        
        if not self.hook_id:
            self.ReportServiceStatus(win32service.SERVICE_STOPPED)
            return

        
        while not self.stop_event.is_set():
            win32event.WaitForSingleObject(self.hWaitStop, 500)

        
        if self.hook_id:
            ctypes.windll.user32.UnhookWindowsHookEx(self.hook_id)

        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(NumpadBlockerService)
