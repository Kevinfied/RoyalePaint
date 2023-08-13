"""
main.py
Kevin Xu

This is the main file for my Paint program. It contains the main loop and is responsible for running the program.
I also define many of the variables here that are used throughout the program. 
In order to run the program, this is the file that must be run.

The description of the program is in the README file.
"""

from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter import filedialog

# These are the separate files that I created
from resources import *
from toolFunctions import *

# Initialize
init()
root = Tk()
root.withdraw()

# Setting up the screen
screen = display.set_mode((1300, 800))
screen.fill(WHITE)
display.set_caption("RoyalePaint")
windowIcon = image.load("resources/stamps/hehehehaw.png")
display.set_icon(windowIcon)

# Background
screen.blit(background, (0, 0))

# Color variables
color = (0, 0, 0, 255)   # Selected Color
pastCols = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)] # Previously used colors
addCol = False   # Flag for adding a color to the pastCols list
oldCol1 = Rect(5, 120, 50, 50)
oldCol2 = Rect(60, 120, 50, 50)
oldCol3 = Rect(115, 120, 50, 50)

# Title
screen.blit(header, (10,10))


# Setting up the canvas
canvasWidth = 960
canvasHeight = 685
canvasRect = Rect(170, 115, 960, 685)
canvas = screen.subsurface((canvasRect))
canvas.fill(WHITE)
userBackground = ""  # User's custom background
customCanvas = False   # Flag for using a custom canvas. Set to false by default

# Initializing the tool variable
tool = "pencil"

# Music
playing = True
mixer.music.load(playlist[currentTrack])
mixer.music.play(-1)


# Color Map
draw.rect(screen, BLACK, (5, 205, 160, 460), 5)
draw.rect(screen, BLACK, (5, 660, 160, 30), 5)
screen.blit(colorMap, (10, 210))
screen.blit(grayscale, (10, 665))

# Shape Tools
fill = True    # Flad for whether or not the shapes are filled
fillText = clashFontS.render("Filled", True, WHITE)
fillText = transform.rotate(fillText, 90)   # Rotates the text so that it is vertical
screen.blit(fillText, (484, 10))
draw.rect(screen, GREEN, fillRect)
screen.blit(fillIcon, (481, 75))


# Stickers
screen.blit(stamp1, (1140, 200))
screen.blit(stamp2, (1140, 280))
screen.blit(stamp3, (1220, 200))
screen.blit(stamp4, (1220, 280))
screen.blit(stamp5, (1140, 360))
screen.blit(stamp6, (1220, 360))


# Thickness Slider
draw.rect(screen, (211, 211, 211), (sliderRect))
sizeArea = screen.subsurface((0, 690, 170, 60))
originalSizeArea = sizeArea.copy()      # Takes a capture of the text area before it gets changed. This will be used to make sure that when the text
screen.blit(sizeText, (sizeTextRect))   # is changed, the old text gets erased. 
draw.rect(screen, (0, 0, 0), ((size * 3) + 7, 728, 4, 14))


# Mouse Coordinates
coordSurface = screen.subsurface((0, 750, 170, 50))
coordCapture = coordSurface.copy()

# Original Music Surface
musicCapture = screen.subsurface((600, 0, 550, 80))
musicCapture = musicCapture.copy()
# Undo and Redo Variables
history = []  # Undo History List
redoHistory = []    # Redo History List
canvasCapture = canvas.copy()
history.append(canvasCapture)

action = False # Flag for whether or not an action was done on the canvas. Whenever action is done on the canvas, a capture of the cnavas will be 
# added to the undo list and redo list will be cleared. 



# Initializing Old Mouse Position Variables
omx, omy = 0, 0
ocx, ocy = 0, 0


## New addition
# undo and redo functions
def undo():
    if len(history) > 1:
        # The following lines takes the newest addition to the undo list, adds it to the redo list,
        # and will then blit it on to the canvas
        redoHistory.append(history.pop())
        canvas.blit(history[-1], (0, 0))

def redo():
    if len(redoHistory) > 0:
        # Takes the newest addition to the redo list, adds it to the undo list, and blits it to the canvas
        history.append(redoHistory.pop())
        canvas.blit(history[-1], (0, 0))

def loadBackground():
    # Lets the user choose the image that they want to load. If the user chose an image, it will
    # load the image and scale it to the size of the canvas, and will then blit it to the canvas.
    loadName = filedialog.askopenfilename()
    if loadName != "":  # Makes sure that the user didnt just quit and chose nothing
        userBackground = image.load(loadName)
        userBackground = transform.scale(userBackground, (canvas.get_width(), canvas.get_height()))
        canvas.blit(userBackground, (0, 0))
        customCanvas = True  # The user has uploaded their own custom background.
        # This will be used for the eraser tool and the clear cavans function.


# Main Loop
running = True
while running:

    ## New addition
    keyArr = key.get_pressed()
    # If ctrl key is held
    if keyArr[K_LCTRL]:
        ctrlFlag = True

    ## Drawing the buttons
    for asset in assetsList:
        screen.blit(asset[0], asset[1])



    # For Ctrl z and y
    # undoFlag = False
    # redoFlag = False

    # Resetting the addCol flag
    addCol = False


    for evt in event.get():
        # Allows the user to quit the program
        if evt.type == QUIT:
            running = False

        if evt.type == MOUSEBUTTONUP:
            if evt.button == 1:
                # On mouse release, 
                # if action was done on the canvas, add a
                # capture of the canvas to the undo list and
                # reset the redo list
                if action:
                    screenCapture = canvas.copy()
                    history.append(screenCapture)
                    redoHistory = []
                    action = False  # Resets the action flag


        if evt.type == KEYDOWN:
            ## New addition
            # Ctrl Z and Y
            # if evt.key == K_LCTRL:
            #     redoFlag = True
            #     undoFlag = True
            #     # if evt.key == K_z:
            #     #     undo()
            #     # elif keyArr[K_y]:
            #     #     redo()
            if evt.key == K_z:
                if ctrlFlag:
                    undo()
            if evt.key == K_y:
                if ctrlFlag:
                    redo()
            # Hotkey for exiting the program
            if evt.key == K_ESCAPE:
                running = False

            if evt.key == K_SPACE:
                # Spacebar will toggle the music
                if playing:
                    mixer.music.pause()
                    playing = False
                else:
                    mixer.music.unpause()
                    playing = True

                # Use the left and arrow keys to toggle through the music
            if evt.key == K_RIGHT:
                if currentTrack < 5:
                    currentTrack += 1
                    mixer.music.stop()  # Stops the current song
                    mixer.music.load(playlist[currentTrack])    # Loads the next song
                    mixer.music.play(-1)    # Start playing the next song (in a loop)
            if evt.key == K_LEFT:
                if currentTrack > 0:
                    currentTrack -= 1
                    mixer.music.stop()
                    mixer.music.load(playlist[currentTrack])
                    mixer.music.play(-1)

            # Use the up and down arrow keys to change the thickness of the tools
            if evt.key == K_UP:
                if size < 50:
                    size += 1
            if evt.key == K_DOWN:
                if size > 1:
                    size -= 1

        ## ON MOUSE BUTTON DOWN
        if evt.type == MOUSEBUTTONDOWN:
            # Allows the user to change the thickness of the tools using the scrollwheel
            if evt.button == 4:
                if size < 50:
                    size += 1
            if evt.button == 5:
                if size > 1:
                    size -= 1


            if evt.button == 1:
                canvasCapture = canvas.copy()  # Takes a capture of the canvas
                shapeOX = ocx    # These are used for the shape tools
                shapeOY = ocy    # They record where the mouse was initially pressed on the canvas when the shape tool was selected

                # Music controls (buttons)
                if nextRect.collidepoint(mx, my):
                    # Allows the user to go to the next song
                    if currentTrack < 5:    # Give that the current song is not the last song in the playlist
                        currentTrack += 1
                        mixer.music.stop()
                        mixer.music.load(playlist[currentTrack])
                        mixer.music.play(-1)

                if backRect.collidepoint(mx, my):
                    # Allows the user to go back to the previous song
                    if currentTrack > 0:   # Given that the current song is not the first song in the playlist
                        currentTrack -= 1
                        mixer.music.stop()
                        mixer.music.load(playlist[currentTrack])
                        mixer.music.play(-1)

                if playRect.collidepoint(mx, my):
                    # Allows the user to toggle the music with the Play button
                    if playing:
                        mixer.music.pause()
                        playing = False
                    else:
                        mixer.music.unpause()
                        playing = True

                if undoRect.collidepoint(mx, my):
                    undo()
# """                    if len(history) > 1:
#                         # The following lines takes the newest addition to the undo list, adds it to the redo list,
#                         # and will then blit it on to the canvas
#                         redoHistory.append(history.pop())
#                         canvas.blit(history[-1], (0, 0))"""

                if redoRect.collidepoint(mx, my):
                    redo()
                    # if len(redoHistory) > 0:
                    #     # Takes the newest addition to the redo list, adds it to the undo list, and blits it to the canvas
                    #     history.append(redoHistory.pop())
                    #     canvas.blit(history[-1], (0, 0))

                if saveRect.collidepoint(mx, my):
                    saveFile(canvas)

                if loadRect.collidepoint(mx, my):
                    loadBackground()
                # Checks which tool the user selects
                if pencilRect.collidepoint(mx, my):
                    tool = "pencil"
                if eraserRect.collidepoint(mx, my):
                    tool = "eraser"
                if brushRect.collidepoint(mx, my):
                    tool = "brush"
                if sprayRect.collidepoint(mx, my):
                    tool = "spray"
                if dropperRect.collidepoint(mx, my):
                    tool = "dropper"
                if highlighterRect.collidepoint(mx, my):
                    tool = "highlighter"
                if calligraphyRect.collidepoint(mx, my):
                    tool = "calligraphy"
                if bucketRect.collidepoint(mx, my):
                    tool = "bucket"
                if lineRect.collidepoint(mx, my):
                    tool = "line"
                if rectangleRect.collidepoint(mx, my):
                    tool = "rectangle"
                if ellipseRect.collidepoint(mx, my):
                    tool = "ellipse"
                if stamp1Rect.collidepoint(mx, my):
                    tool = "stamp1"
                if stamp2Rect.collidepoint(mx, my):
                    tool = "stamp2"
                if stamp3Rect.collidepoint(mx, my):
                    tool = "stamp3"
                if stamp4Rect.collidepoint(mx, my):
                    tool = "stamp4"
                if stamp5Rect.collidepoint(mx, my):
                    tool = "stamp5"
                if stamp6Rect.collidepoint(mx, my):
                    tool = "stamp6"


                # User Color Picking
                if colorMapRect.collidepoint(mx, my):
                    # Gets the color of the pixel that the user clicked on (with the offset of the color map)
                    color = colorMap.get_at((mx - 10, my - 210))
                    addCol = True  # Toggles the flag to true. This will allow the program to add the color to the previously used colors list
                if grayscaleRect.collidepoint(mx, my):
                    color = grayscale.get_at((mx - 10, my - 665))
                    addCol = True

                # Clear Canvas
                if clearRect.collidepoint(mx, my):
                    # Clears the canvas and adds the cleared canvas to the history list
                    clearCanva(canvas, customCanvas, userBackground)
                    screenCapture = canvas.copy()
                    history.append(screenCapture)
                    redoHistory = []  # Clears redo list


                # Tool actions
                if canvasRect.collidepoint(mx, my):
                    ## Tool functions are explained in toolFunctions.py
                    # Bucket Tool
                    if tool == "bucket":
                        bucketTool(canvas, cx, cy, color)
                        # cx and cy are later defined in the code.

                    # Eye Dropper Tool
                    if tool == "dropper":
                        color = dropperTool(canvas, cx, cy)



                # Toggling the fill for the shape tools
                if fillRect.collidepoint(mx, my):
                    if fill == True:
                        draw.rect(screen, RED, (fillRect))
                        screen.blit(unfillIcon, (481, 76))
                        fill = False
                    elif fill == False:
                        draw.rect(screen, GREEN, (fillRect))
                        screen.blit(fillIcon, (fillRect))
                        fill = True

                # Checking if user chooses to use previously-selected colors
                if oldCol1.collidepoint(mx, my):
                    color = pastCols[-2]
                if oldCol2. collidepoint(mx, my):
                    color = pastCols[-3]
                if oldCol3.collidepoint(mx, my):
                    color = pastCols[-4]




    # Mouse Position
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    # Position of mouse on canvas (with the offset)
    cx, cy = mx - 170, my - 115
    # The reason these variables are here and not earlier is because for some reason, they interfere with the undo/redo function. 



    # Coordinates of the mouse on the canvas
    screen.blit(coordCapture, (0, 750))  # Resetting the coordinates background.
    coords = clashFontS.render("(%d, %d)" % (cx, cy), True, WHITE)
    coordsRect = coords.get_rect()  # Centers the coordinates text to (85, 775)
    coordsRect.center = (85, 775)
    if canvasRect.collidepoint(mx, my):   # Only display the coordinates if the mouse is on the canvas
        screen.blit(coords, (coordsRect))

    # Size Slider
    sizeText = clashFontL.render("%d" % (size), True, WHITE)
    textRect = sizeText.get_rect()
    textRect.center = (85, 710)    # Centers the size text to (85, 710)

    if sliderRect.collidepoint(mx, my):
        if mb[0]:
            size = (mx - 7)//3      # The size of the tools is determined by the position of the mouse on the slider
                                    # Sorry for the weird math


    screen.blit(originalSizeArea, (0, 690))
    screen.blit(sizeText, (textRect))   # Displays the size of the tools centered at (85, 710)
    draw.rect(screen, BLACK, ((size * 3) + 7, 728, 4, 14))  # drawss the slider


    # Display Current Track Being Played
    screen.blit(musicCapture, (600, 0))
    musicDisplay = clashFontM.render(soundtrackNames[currentTrack], True, WHITE)
    musicDisplayRect = musicDisplay.get_rect()
    musicDisplayRect.center = (835, 40)
    screen.blit(musicDisplay, (musicDisplayRect))


    # Highlights the button that the user is hovering over with a red border
    if mb[0] == 0:
        if pencilRect.collidepoint(mx, my):
            draw.rect(screen, RED, (pencilRect), 2)
        elif eraserRect.collidepoint(mx, my):
            draw.rect(screen, RED, (eraserRect), 2)
        elif brushRect.collidepoint(mx, my):
            draw.rect(screen, RED, (brushRect), 2)
        elif sprayRect.collidepoint(mx, my):
            draw.rect(screen, RED, (sprayRect), 2)
        elif dropperRect.collidepoint(mx, my):
            draw.rect(screen, RED, (dropperRect), 2)
        elif highlighterRect.collidepoint(mx, my):
            draw.rect(screen, RED, (highlighterRect), 2)
        elif calligraphyRect.collidepoint(mx, my):
            draw.rect(screen, RED, (calligraphyRect), 2)
        elif bucketRect.collidepoint(mx, my):
            draw.rect(screen, RED, (bucketRect), 2)
        elif lineRect.collidepoint(mx, my):
            draw.rect(screen, RED, (lineRect), 2)
        elif rectangleRect.collidepoint(mx, my):
            draw.rect(screen, RED, (rectangleRect), 2)
        elif ellipseRect.collidepoint(mx, my):
            draw.rect(screen, RED, (ellipseRect), 2)
        elif undoRect.collidepoint(mx, my):
            draw.rect(screen, RED, (undoRect), 2)
        elif redoRect.collidepoint(mx, my):
            draw.rect(screen, RED, (redoRect), 2)
        elif saveRect.collidepoint(mx, my):
            draw.rect(screen, RED, (saveRect), 2)
        elif loadRect.collidepoint(mx, my):
            draw.rect(screen, RED, (loadRect), 2)
        elif clearRect.collidepoint(mx, my):
            draw.rect(screen, RED, (clearRect), 2)
        elif nextRect.collidepoint(mx, my):
            screen.blit(nextHover, (nextRect))
        elif backRect.collidepoint(mx, my):
            screen.blit(backHover, (backRect))
        elif playRect.collidepoint(mx, my):
            screen.blit(playHover, (playRect))


    # Highlights the tool that is currently selected with a green border around the button. 
    if tool == "pencil":
        draw.rect(screen, GREEN, (pencilRect), 2)
    if tool == "eraser":
        draw.rect(screen, GREEN, (eraserRect), 2)
    if tool == "brush":
        draw.rect(screen, GREEN, (brushRect), 2)
    if tool == "spray":
        draw.rect(screen, GREEN, (sprayRect), 2)
    if tool == "dropper":
        draw.rect(screen, GREEN, (dropperRect), 2)
    if tool == "highlighter":
        draw.rect(screen, GREEN, (highlighterRect), 2)
    if tool == "calligraphy":
        draw.rect(screen, GREEN, (calligraphyRect), 2)
    if tool == "bucket":
        draw.rect(screen, GREEN, (bucketRect), 2)
    if tool == "line":
        draw.rect(screen, GREEN, (lineRect), 2)
    if tool == "rectangle":
        draw.rect(screen, GREEN, (rectangleRect), 2)
    if tool == "ellipse":
        draw.rect(screen, GREEN, (ellipseRect), 2)









    # On Left Hold
    if mb[0]:
        if canvasRect.collidepoint(mx, my):
            action = True  # Action has been done on the canvas

            # All the tool functions are exaplined in the toolFunctions.py file
            if tool == "pencil":
                pencilTool(canvas, color, ocx, ocy, cx, cy, 3)

            if tool == "eraser":
                eraserTool(canvas, ocx, ocy, cx, cy, size, customCanvas, userBackground)

            if tool == "spray":
                sprayTool(canvas, color, cx, cy, size)

            if tool == "brush":
                brushTool(canvas, color, ocx, ocy, cx, cy, size)

            if tool == "line":
                lineTool(canvas, shapeOX, shapeOY, cx, cy, color, size, canvasCapture)

            if tool == "rectangle":
                rectangleTool(canvas, shapeOX, shapeOY, cx, cy, color, size, canvasCapture, fill)

            if tool == "calligraphy":
                calligraphyTool(canvas, ocx, ocy, cx, cy, color, size)

            if tool == "ellipse":
                circleTool(canvas, shapeOX, shapeOY, cx, cy, color, size, canvasCapture, fill)

            if tool == "highlighter":
                highlighterTool(canvas, color, ocx, ocy, cx, cy, size)

            if tool == "stamp1":
                # Blits the canvas capture to the screen so that the stamp is only drawn on the canvas when the mouse button is let go of
                screen.blit(canvasCapture,(170, 115))
                canvas.blit(stamp1, (cx - 35, cy - 35))

            if tool == "stamp2":
                screen.blit(canvasCapture,(170, 115))
                canvas.blit(stamp2, (cx - 35, cy - 35))

            if tool == "stamp3":
                screen.blit(canvasCapture,(170, 115))
                canvas.blit(stamp3, (cx - 35, cy - 35))

            if tool == "stamp4":
                screen.blit(canvasCapture,(170, 115))
                canvas.blit(stamp4, (cx - 35, cy - 35))

            if tool == "stamp5":
                screen.blit(canvasCapture,(170, 115))
                canvas.blit(stamp5, (cx - 35, cy - 35))

            if tool == "stamp6":
                screen.blit(canvasCapture,(170, 115))
                canvas.blit(stamp6, (cx - 35, cy - 35))


    # Adding previous colors to the pastCols list
    if addCol:
        # If the addCols flag is true, the current color is added to the pastCols list
        pastCols.append(color)
    # Displaying the last three used colors (not including the current color)
    draw.rect(screen, pastCols[-2], oldCol1)
    draw.rect(screen, pastCols[-3], oldCol2)
    draw.rect(screen, pastCols[-4], oldCol3)

    draw.rect(screen, color, (10, 185, 150, 20))    # Displays the current color being used to the user
    draw.rect(screen, BLACK, (5, 180, 160, 30), 5)  # A border around the current color

    # Old Mouse Positions
    omx = mx
    omy = my
    ocx = cx
    ocy = cy

    # Updates the display
    display.flip()

# Stops the music and quits the program
mixer.music.stop()
quit()