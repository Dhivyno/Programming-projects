import pyautogui as pg
import time

key = str(input("What key do you want to press repeatedly (mouse button if you want to click): "))
speed = int(input("How many times a second do you want to click or press a key max 10: "))
while speed > 10:
    speed = int(input("Please enter a number below 10: "))
times = int(input("How many times do you want to press the key: "))

time.sleep(5)

if key in ["mouse button", "Mouse button", "MOUSE BUTTON"]:
    for i in range(times):
        pg.click()
        time.sleep((1 / speed) - 0.1)
else:
    for i in range(times):
        pg.press(key)
        time.sleep((1/speed)-0.1)
