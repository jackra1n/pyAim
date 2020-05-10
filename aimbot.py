import pyautogui
import time
import os

# screenshotCords = [0,120,1900,530 ]
x = 0
while True:
    if x >= 30:
        end = pyautogui.locateOnScreen("end.png", grayscale=True, confidence=.7)
        if end is not None:
            exit()
    target = pyautogui.locateOnScreen("target.png", grayscale=True, confidence=.5)
    if target is None:
        print("could not find target")
    else:
        print(target)
        pyautogui.click(target[0]+(target[2]/2), target[1]+(target[3]/2))
        x += 1
        time.sleep(.05)
