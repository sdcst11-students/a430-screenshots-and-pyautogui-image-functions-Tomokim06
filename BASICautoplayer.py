import pyautogui
import time
import os

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

def bonus():
        m = 0
        pyautogui.moveTo(380, 665)
        while m < 21:
            x, y = pyautogui.position()
            px = pyautogui.pixel(x, y)

            if px == (221, 136, 0):
                #yellow ^^^
                m = m+1
                pyautogui.moveTo(x+45, y)
                print(f"{m}")
            else:
                print("else")
                def column(x):
                    pyautogui.moveTo(x, 143)
                    #136 is top square
                    k = 0
                    while k < 12:
                        x, y = pyautogui.position()
                        px = pyautogui.pixel(x, y)

                        if px == (136, 204, 68):
                            #green ^^^
                            k = k+1
                            pyautogui.moveTo(x, y+44)
                        else:
                            x, y = pyautogui.position()
                            #buy building to next level
                            pyautogui.moveTo(1087,100)
                            pyautogui.click(1)
                            pyautogui.moveTo(220, y)
                            pyautogui.doubleClick(20)
                    column()




def next():
    pyautogui.moveTo(1260, 100)
    pyautogui.click()




#x = 0
#while x < 2:
#    main()
#    x = x+1

bonus()