#include <windows.h>
#include <iostream>

HHOOK hHook = NULL;

LRESULT CALLBACK LowLevelKeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (nCode == HC_ACTION) {
        KBDLLHOOKSTRUCT *pKeyboard = (KBDLLHOOKSTRUCT *)lParam;
        if (wParam == WM_KEYDOWN || wParam == WM_SYSKEYDOWN) {
            if((pKeyboard->vkCode == VK_DELETE) && (GetAsyncKeyState(VK_CONTROL) && 0x8000) && (GetAsyncKeyState(VK_MENU) & 0x8000)){
                return 1;
            }
        }
    }
    return CallNextHookEx(hHook, nCodem wParam, lParam);
}

void SetHook() {
    hHook = SetWindowsHookEx(WH_KEYBOARD_LL, LowLevelKeyboardProc, NULL, 0);
    if (!hHook) {
        std::cerr << "Failed to install hook!" << std::endl;
    }
}

void Unhook() {
    if (hHook) {
        UnhookWindowsHookEx(hHook);
    }
}

int main() {
    SetHook();

    MSG msg;
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    Unhook();
    return 0;
}