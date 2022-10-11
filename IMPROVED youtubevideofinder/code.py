import pyautogui as pg
import time

print("Instructions: Enter video name and desktop name and then switch over to a new tab in google "
      "within the 3 second delay. You also need to have the youtube search bar and google search bar picture downloaded on your pictures directory")
print("The program will automatically play the video and also avoid any ad videos "
      "that appear on top when searching for the specified video")

vid_name = input("What is the name of the video you want to open? ")
desktop_name = str(input("What is your desktop name?  "))

time.sleep(3)

def path(name):
    return str('C:\\Users\\'+desktop_name+'\\OneDrive\\Pictures\\' + name)


google_search_bar = pg.locateCenterOnScreen(path("google_search_bar.png"), confidence=0.9)
pg.click(google_search_bar)
pg.write("https://www.youtube.com/")
pg.press("Enter")
time.sleep(6)
youtube_search_bar = pg.locateCenterOnScreen(path("youtube_search_bar.png"), confidence=0.9)
pg.click(youtube_search_bar)
time.sleep(2)
pg.write(vid_name)
pg.press("Enter")

time.sleep(4)

myScreenshot = pg.screenshot()
myScreenshot.save('C:\\Users\\'+desktop_name+'\\OneDrive\\Desktop\\ss.png')

from PIL import Image

im = Image.open('C:\\Users\\'+desktop_name+'\\OneDrive\\Desktop\\ss.png')
coordinate = x, y = 913, 260
check = im.getpixel(coordinate)
if check != (255, 255, 241): #checks if specified pixel if a white shade indicating whether or not the corresponding video is an ad
    pg.click(708, 304)
else:
    pg.click(708, 529)  #if first video is an ad, clicks on second video


