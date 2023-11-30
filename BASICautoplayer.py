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
        while m < 21:
            pyautogui.moveTo(380, 665)
            x, y = pyautogui.position()
            px = pyautogui.pixel(x, y)

            if px == (221, 136, 0):
                #yellow ^^^
                m = m+1
                px = (x+45, y)
                print(f"{m}")
            else:
                print(f"else{x}")
                def column(x):
                    pyautogui.moveTo(x, 136)
                    #136 is top square
                    k = 1
                    while k == 1:
                        x, y = pyautogui.position()
                        px = pyautogui.pixel(x, y)
                        if px == (136, 204, 68):
                            y = y+44
                        else:
                            k = 5  
                            #buy building to next level
                            pyautogui.moveTo(1087,100)
                            pyautogui.moveTo(220, y)
                            x, y = pyautogui.position()
                            px = pyautogui.pixel(x, y)
                            if px == (85, 119, 255):
                                pyautogui.click(25)
                                #keep trying new columns

 
                column()




def next():
    pyautogui.moveTo(1260, 100)
    pyautogui.click()




#x = 0
#while x < 2:
#    main()
#    x = x+1

bonus()