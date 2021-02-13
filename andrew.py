import time 
import pyautogui

while True:
    pyautogui.moveTo(100, 100, duration = 0.1) 
    time.sleep(5)  
    pyautogui.moveTo(150, 150, duration = 0.1) 
    time.sleep(5)
