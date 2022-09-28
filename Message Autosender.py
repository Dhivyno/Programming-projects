import pyautogui as pg
import time

print("Instructions: There will be a 5 second delay between your 'How many times' "
      "input and the autosend so within this time, go to the type box of the app that you want to autosend in")
msg = input("What do you want to autosend? ")
times = int(input("How many times do you want to send this message? "))

time.sleep(5)

for i in range(times):
    pg.write(msg)
    pg.press("Enter")
    time.sleep(0.1)
