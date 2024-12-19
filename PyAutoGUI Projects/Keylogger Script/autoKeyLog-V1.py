# V1.0
# 5-Dec-2024 (Last date modified)
# Code by Danton Alexander
# Install pyautogui (pip install pyautogui)
# Test in inclosed environment, the mouse will move/click & keys will be pressed.
# Tests start on line 142


import time
import pyautogui


# Keys mapped
VK_CODE = {
    'backspace': 'backspace',
    'tab': 'tab', 
    'enter': 'enter', 
    'shift': 'shift', 
    'ctrl': 'ctrl', 
    'alt': 'alt',
    'caps_lock': 'capslock', 
    'esc': 'esc', 
    'spacebar': 'space', 
    'page_up': 'pageup', 
    'page_down': 'pagedown',
    'end': 'end', 
    'home': 'home', 
    'left_arrow': 'left', 
    'up_arrow': 'up', 
    'right_arrow': 'right', 
    'down_arrow': 'down',
    '0': '0', 
    '1': '1', 
    '2': '2', 
    '3': '3', 
    '4': '4', 
    '5': '5', 
    '6': '6', 
    '7': '7', 
    '8': '8', 
    '9': '9',
    'a': 'a', 
    'b': 'b', 
    'c': 'c', 
    'd': 'd', 
    'e': 'e', 
    'f': 'f', 
    'g': 'g', 
    'h': 'h', 
    'i': 'i', 
    'j': 'j', 
    'k': 'k',
    'l': 'l', 
    'm': 'm', 
    'n': 'n', 
    'o': 'o', 
    'p': 'p', 
    'q': 'q', 
    'r': 'r', 
    's': 's', 
    't': 't', 
    'u': 'u', 
    'v': 'v',
    'w': 'w', 
    'x': 'x', 
    'y': 'y', 
    'z': 'z', 
    'numpad_0': 'num0', 
    'numpad_1': 'num1', 
    'numpad_2': 'num2', 
    'numpad_3': 'num3',
    'numpad_4': 'num4', 
    'numpad_5': 'num5', 
    'numpad_6': 'num6', 
    'numpad_7': 'num7', 
    'numpad_8': 'num8', 
    'numpad_9': 'num9',
    'add_key': '+', 
    'subtract_key': '-', 
    'decimal_key': '.', 
    'divide_key': '/', 
    'multiply_key': '*',
    'F1': 'f1', 
    'F2': 'f2', 
    'F3': 'f3', 
    'F4': 'f4', 
    'F5': 'f5', 
    'F6': 'f6', 
    'F7': 'f7', 
    'F8': 'f8', 
    'F9': 'f9',
    'F10': 'f10', 
    'F11': 'f11', 
    'F12': 'f12'
}

#Mouse move and click (movement by px in tests)
def click_mouse(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

#Key press
def press(*args):
    for key in args:
        pyautogui.press(VK_CODE.get(key, key))

#Key press and hold
def press_and_hold(*args):
    for key in args:
        pyautogui.keyDown(VK_CODE.get(key, key))

#Key release held key
def release(*args):
    for key in args:
        pyautogui.keyUp(VK_CODE.get(key, key))

#Key press/hold/release
def press_hold_release(*args):
    for key in args:
        pyautogui.keyDown(VK_CODE.get(key, key))
    for key in args:
        pyautogui.keyUp(VK_CODE.get(key, key))

#Typing with special characters handling
def typer(string):
    time.sleep(1)
    for char in string:
        if char in VK_CODE:
            pyautogui.press(VK_CODE[char])
        elif char.isupper():
            pyautogui.keyDown('shift')
            pyautogui.press(char.lower())
            pyautogui.keyUp('shift')
        else:
            pyautogui.press(char)



##################################################################################################################
# TEST #

if __name__ == "__main__":
    click_mouse(100, 200)  # Move to x/y position and click
    press('enter')  # Press key
    press_and_hold('ctrl', 'c')  # Press and hold key
    time.sleep(1)
    release('ctrl', 'c')  # Release key
    typer("Testing typing!")  

