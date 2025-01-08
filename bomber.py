import pyautogui
import time  # Import the time module

def bomber():
    pyautogui.typewrite("BOMBER HU")
    pyautogui.keyDown("enter")

for i in range(100):
    bomber()
    time.sleep(0.5)  # Pause for 1 second between messages