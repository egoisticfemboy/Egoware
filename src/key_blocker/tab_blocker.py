import keyboard

def block_tab_key(event):
    if event.name == 'tab':
        return False
    

keyboard.hook(block_tab_key)


print("Skill issue UwU")
