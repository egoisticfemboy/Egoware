import keyboard
import os
def block_f11_key(event):
    if event.name == 'f11':
        return False
    
keyboard.hook(block_f11_key)

print("Skill issue UwU")
keyboard.wait()