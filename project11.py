import pyautogui
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen('1.png')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('2.png')
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen('3.png')
    print(picPosition)
