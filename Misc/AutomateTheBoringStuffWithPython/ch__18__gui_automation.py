import pyautogui, time, os

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = 1

width, height = resolution = pyautogui.size()

print(f"Width:{width}, Height:{height}")


def currentMousePosition():
    return pyautogui.position()


def moveInSquare():
    for i in range(10):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)


def moveInSquareRelative():
    while True:
        print("Moving mouse again")

        for i in range(10):
            pyautogui.moveRel(100, 0, duration=0.25)
            pyautogui.moveRel(0, 100, duration=0.25)
            pyautogui.moveRel(-100, 0, duration=0.25)
            pyautogui.moveRel(0, -100, duration=0.25)

# print(f"Current Mouse Position:{currentMousePosition()}")
moveInSquareRelative()

def clickLocation():
    clickLocation = (1400, 800)
    print("Clicking at:", clickLocation)
    pyautogui.click(clickLocation[0], clickLocation[1], button='right')


def drawSpiral():
    DUR = .2
    time.sleep(5)
    pyautogui.click()
    distance = 200

    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=DUR)
        distance -= 5
        pyautogui.dragRel(0, distance, duration=DUR)
        pyautogui.dragRel(-distance, 0, duration=DUR)
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=DUR)


# drawSpiral()

def scrollTest():
    pyautogui.click()
    pyautogui.scroll(200)


# scrollTest()


def imageRecognition():
    print('hi')
    print(os.listdir())
    RECOGNITION_FILE = os.getcwd() + '/imageRecognition.png'
    print(RECOGNITION_FILE)
    pyautogui.locateOnScreen(RECOGNITION_FILE)

# imageRecognition()


def typeTest():
    DELAY = .25
    pyautogui.click(1400, 300)
    pyautogui.typewrite('Hello World', DELAY)

# typeTest()
