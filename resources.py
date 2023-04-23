"""
resources.py
Kevin Xu

This file loads all the resources for the program. 
It loads all the images for the buttons and resize them to fit the program.
It also contains the pre-defined colours and the font used in the program.


There are not a lot of comments in this file because I feel like there is really no point in explaining them. I am 
really only just loading assets from the resources folder so I can use them in main.py
"""


from pygame import *
from random import *
# pre-defined colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
CYAN = (0, 125, 125)
WHITE = (255, 255, 255)
RANcol = (randint(0, 255)), (randint(0, 255)), (randint(0, 255))


# Background
background = image.load("resources/gui/clashBackground.png")
background = transform.scale(background, (1300, 800))

# Title
header = image.load("resources/gui/clashHeader.png")
header = transform.scale(header, (220, 100))

# Music
# I am loading all of the soundtracks into a list.
playlist = ["resources/music/1.mainmenu.wav", "resources/music/2.battle1.wav", "resources/music/3.battle2.wav",
"resources/music/4.battle3.wav", "resources/music/5.suddendeath.wav", "resources/music/6.suddendeathold.wav"]

# This is the list of names for the soundtracks. Easier to dispplay.
soundtrackNames = ["1. Main Menu", "2. Battle 1", "3. Battle 2", "4. Battle 3", "5. Sudden Death",
"6. Sudden Death (Old Version)"]
currentTrack = 0


# Font
font.init()
clashFontS = font.Font("resources/font/CR.ttf", 14)
clashFontM = font.Font("resources/font/CR.ttf", 20)
clashFontL = font.Font("resources/font/CR.ttf", 25)

# Music Controls
nextRect = Rect(880, 80, 30, 30)
backRect = Rect(760, 80, 30, 30)
playRect = Rect(820, 80, 30, 30)

nextIcon = image.load("resources/icons/next.png")
backIcon = image.load("resources/icons/back.png")
playIcon = image.load("resources/icons/play.png")

# These are the images that will be displayed when the mouse hovers over the music control buttons. 
nextHover = image.load("resources/icons/nextHover.png")
backHover = image.load("resources/icons/backHover.png")
playHover = image.load("resources/icons/playHover.png")

nextIcon = transform.scale(nextIcon, (30, 30))
backIcon = transform.scale(backIcon, (30, 30))
playIcon = transform.scale(playIcon, (30, 30))
nextHover = transform.scale(nextHover, (30, 30))
backHover = transform.scale(backHover, (30, 30))
playHover = transform.scale(playHover, (30, 30))



# Color Map
colorMap = image.load("resources/gui/colorMap.png")
colorMap = transform.scale(colorMap, (150, 450))
grayscale = image.load("resources/gui/grayscale.png")
grayscale = transform.scale(grayscale, (150, 20))
colorMapRect = Rect(10, 210, 150, 450)
grayscaleRect = Rect(10, 665, 150, 20)


# Pencil Icon
pencilRect = Rect(250, 5, 50, 50)
pencilIcon = image.load("resources/icons/pencil.png")
pencilIcon = transform.scale(pencilIcon, (50, 50))


# Brush Icon
brushRect = Rect(250, 60, 50, 50)
brushIcon = image.load("resources/icons/brush.png")
brushIcon = transform.scale(brushIcon, (50, 50))


# Eraser Icon
eraserRect = Rect(305, 5, 50, 50)
eraserIcon = image.load("resources/icons/eraser.png")
eraserIcon = transform.scale(eraserIcon, (50, 50))


# Spray Paint Icon
sprayRect = Rect(305, 60, 50, 50)
sprayIcon = image.load("resources/icons/spray.png")
sprayIcon = transform.scale(sprayIcon, (50, 50))


# Calligraphy Pen Icon
calligraphyRect = Rect(360, 60, 50, 50)
calligraphyIcon = image.load("resources/icons/calligraphy.png")
calligraphyIcon = transform.scale(calligraphyIcon, (50, 50))


# Eye dropper Icon
dropperRect = Rect(360, 5, 50, 50)
dropperIcon = image.load("resources/icons/dropper.png")
dropperIcon = transform.scale(dropperIcon, (50, 50))


# Highlighter Icon
highlighterRect = Rect(415, 5, 50, 50)
highlighterIcon = image.load("resources/icons/highlighter.png")
highlighterIcon = transform.scale(highlighterIcon, (50, 50))


# Bucket Icon
bucketRect = Rect(415, 60, 50, 50)
bucketIcon = image.load("resources/icons/bucket.png")
bucketIcon = transform.scale(bucketIcon, (50, 50))


## SHAPE TOOLS
# Line Tool
lineRect = Rect(525, 4, 33, 33)
lineIcon = image.load("resources/icons/line.png")
lineIcon = transform.scale(lineIcon, (33, 33))

# Rectangle Tool
rectangleRect = Rect(525, 41, 33, 33)
rectangleIcon = image.load("resources/icons/rectangle.png")
rectangleIcon = transform.scale(rectangleIcon, (33, 33))

# Ellipse Tool
ellipseRect = Rect(525, 78, 33, 33)
ellipseIcon = image.load("resources/icons/circle.png")
ellipseIcon = transform.scale(ellipseIcon, (33, 33))

# Fill Icon
fillRect = Rect(480, 75, 30, 30)
fillIcon = image.load("resources/icons/fill.png")
fillIcon = transform.scale(fillIcon, (28, 28))
unfillIcon = image.load("resources/icons/unfill.png")
unfillIcon = transform.scale(unfillIcon, (28, 28))



# Save Icon
saveRect = Rect(1240, 5, 50, 50)
saveIcon = image.load("resources/icons/save.png")
saveIcon = transform.scale(saveIcon, (50, 50))


# Load Icon
loadRect = Rect(1180, 5, 50, 50)
loadIcon = image.load("resources/icons/load.png")
loadIcon = transform.scale(loadIcon, (50, 50))


## STAMPS
# Stamp 1 - Laughing King
stamp1Rect = Rect(1140, 200 , 70, 70)
stamp1 = image.load("resources/stamps/hehehehaw.png")
stamp1 = transform.scale(stamp1, (70, 70))
# Stamp 2 - Angry King
stamp2Rect = Rect(1140, 280 , 70, 70)
stamp2 = image.load("resources/stamps/GRRRRR.png")
stamp2 = transform.scale(stamp2, (70, 70))
# Stamp 3 - Crying King
stamp3Rect = Rect(1220, 200, 70, 70)
stamp3 = image.load("resources/stamps/buhuhuhu.png")
stamp3 = transform.scale(stamp3, (70, 70))
# Stamp 4 - Thumbs Up King
stamp4Rect = Rect(1220, 280, 70, 70)
stamp4 = image.load("resources/stamps/thumbsup.png")
stamp4 = transform.scale(stamp4, (70, 70))
# Stamp 5 - Crying Skeleton
stamp5Rect = Rect(1140, 360, 70, 70)
stamp5 = image.load("resources/stamps/mimimimi.png")
stamp5 = transform.scale(stamp5, (70, 70))
# Stamp 6 - Hog Rider
stamp6Rect = Rect(1220, 360, 70, 70)
stamp6 = image.load("resources/stamps/hogrider.png")
stamp6 = transform.scale(stamp6, (70, 70))


# Undo and Redo Icons
undoRect = Rect(1135, 740, 50, 50)
undoIcon = image.load("resources/icons/undo.png")
undoIcon = transform.scale(undoIcon, (50, 50))

redoRect = Rect(1190, 740, 50, 50)
redoIcon = image.load("resources/icons/redo.png")
redoIcon = transform.scale(redoIcon, (50, 50))

# Clear Icon
clearRect = Rect(1245, 740, 50, 50)
clearIcon = image.load("resources/icons/clear.png")
clearIcon = transform.scale(clearIcon, (50, 50))



# Thickness Slider
sliderRect = Rect(10, 730, 150, 10)
size = 10   # Default size
sizeText = clashFontL.render("%d" % (size), True, (255, 255, 255)) # The text that will display the tool size on the screen
sizeTextRect = sizeText.get_rect()
sizeTextRect.center = (85, 710)   # Setting the center of the text to (85, 710)








