import pyautogui, time, keyboard
pyautogui.PAUSE = 0.0001

def idle():
    if keyboard.is_pressed("q"):
        quit()
    x = 200
    y = 150
    pyautogui.moveTo(x, y)
    pyautogui.click()

    a = 1
    while a < 13:
        pyautogui.moveTo(x,y+44)
        pyautogui.click()
        y = y+44
        a = a+1

def column():
    x, y = pyautogui.position()
    pyautogui.moveTo(x, 143)
    #y=143 is top square
    k = 0
    while k < 13:
        x, y = pyautogui.position()
        px = pyautogui.pixel(x, y)

        if px == (136, 204, 68):
            #green ^^^
            k = k+1
            pyautogui.moveTo(x, y+45)
        else:
            #print(x,y)
            #quit()
            k = 99
            x, y = pyautogui.position()
            px = pyautogui.pixel(x, y)
            #buy building to next level
            pyautogui.moveTo(1087,100)
            pyautogui.click()
            pyautogui.moveTo(220, y)
            #Buy new buildings until color is green and not grey(34, 34, 34)
            while px == (34, 34, 34):
                if keyboard.is_pressed("q"):
                    quit()
                pyautogui.click()
                px = pyautogui.pixel (x,y)
                if px != (34, 34, 34):
                    break

def bonus():
        m = 0
        pyautogui.moveTo(380, 710)
        while m < 21:
            x, y = pyautogui.position()
            px = pyautogui.pixel(x, y)
            if px == (221, 136, 0):
                #orange ^^^
                m = m+1
                pyautogui.moveTo(x+45, y)
            else:
                m = 999
                column()

#def next():
#    pyautogui.moveTo(1260, 100)
#    pyautogui.click()

def main():
    while True:
        for i in range(5):
            idle()
        bonus()
        time.sleep(2)

def timer():
    if __name__ == '__main__':
        start_time = time.time()
        for i in range (1):
            idle()
        print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
        
