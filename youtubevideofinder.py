import pyautogui as pg
import time

print("Instructions: Enter video name and desktop name and then switch over to a new tab in google "
      "within the 5 second delay.")
print("The program will automatically play the video and also avoid any ad videos "
      "that appear on top when searching for the specified video")
name = input("What is the name of the video you want to open? ")
desktopname = str(input("What is your desktop name?  "))
path = 'C:\\Users\\'+desktopname+'\\OneDrive\\Desktop\\ss.png'

time.sleep(5)

pg.click(855, 66)
pg.write("youtube")
pg.press("Enter")
time.sleep(3)
pg.click(294, 367) #clicks on first result of search in google
time.sleep(5)
pg.click(765, 119) #clicks on search bar
pg.write(name)
pg.press("Enter")
time.sleep(5)

myScreenshot = pg.screenshot()
myScreenshot.save(path)

#use 'mrbeast chocolate factory" for ad vid skip test
from PIL import Image

im = Image.open(path)
coordinate = x, y = 913, 260
check = im.getpixel(coordinate)
if check != (255, 255, 241): #checks if specified pixel if a white shade indicating whether or not the corresponding video is an ad
    pg.click(708, 304)
else:
    pg.click(708, 529)  #if first video is an ad, clicks on second video
