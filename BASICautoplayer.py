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
    while True:
        m = 0
        while m < 21:
            pyautogui.moveTo(380, 665)
            x, y = pyautogui.position()
            px = pyautogui.pixel(x, y)

            if px == (221, 136, 0):
                #yellow ^^^
                m = m+1
                px = (x+45, y)
                print("1")
            else:
                print(f"else{x}")
                def column(x):
                    pyautogui.moveTo(x, 136)
                    x, y = pyautogui.position()
                    px = pyautogui.pixel(x, y)
                    if px == (136, 204, 68):
                        #move down column and keep looking
                    #else:
                        #buy building to next level
                        pyautogui.moveTo(1260,100)
                        pyautogui.moveTo(220, y)
                        x, y = pyautogui.position()
                        px = pyautogui.pixel(x, y)
                        if px == (85, 119, 255):
                            #blue
                            pyautogui.click()
                            #keep trying new columns
                        if px == (52, 54, 56) or px == (31, 31, 31):
                            #greys
                            while px == (52, 54, 56) or px == (31, 31, 31):
                                #VVV  pause until grey turns blue  VVV
                                os.system("pause")
                column()




def next():
    pyautogui.moveTo(1260, 100)
    pyautogui.click()




#x = 0
#while x < 2:
#    main()
#    x = x+1

bonus()