import subprocess
import winreg

def enable_virtual_keyboard():
    try:
        reg_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_key, 0, winreg.KEY_SET_VALUE)
        
        winreg.SetValueEx(key, "Osk", 0, winreg.REG_SZ, "C:\\Windows\System32\osk.exe")
        winreg.CloseKey(key)
        
        print("Virtual keyboard enabled")
        
    except Exception as e:
        print(f"Failed to enable virtual keyboard: {e}")
        
def disable_power_button():
    try:
        
        reg_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"

        
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_key, 0, winreg.KEY_SET_VALUE)

        
        winreg.SetValueEx(key, "ShutdownWithoutLogon", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)

        print("Power button disabled.")
    except Exception as e:
        print(f"Failed to disable power button: {e}")
        
        
if __name__ == "__main__":
    enable_virtual_keyboard()
    disable_power_button()
