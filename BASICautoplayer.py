import pyautogui
import time

def main():
    x = 200
    y = 150
    pyautogui.moveTo(x, y)
    pyautogui.click()

    a = 1
    while a < 12:
        pyautogui.moveTo(x,y+44)
        pyautogui.click()
        y = y+44
        a = a+1

def next():
    pyautogui.moveTo(1260, 100)
    pyautogui.click()

x = 0
while x < 2:
    main()
    x = x+1

