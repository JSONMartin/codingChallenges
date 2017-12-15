import pyautogui

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
    for i in range(10):
        pyautogui.moveRel(100, 0, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)

print(f"Current Mouse Position:{currentMousePosition()}")
moveInSquareRelative()
