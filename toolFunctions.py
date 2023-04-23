"""
toolFunctions.py
Kevin Xu

This is where I define all the tool functions for the program.
"""

from pygame import *
from random import *
from math import *


# Pre defined colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
CYAN = (0, 125, 125)
WHITE = (255, 255, 255)


# Pencil Tool
def pencilTool(surface, color, ox, oy, x, y, size):
    draw.line(surface, color, (ox, oy), (x, y), size) # Drawing a line from the old mouse position to the new mouse position


# Spray Tool
def sprayTool(surface, color, x, y, radius):
    # Randomly generates values for the x and y coordinates of the point (relative to the mouse position)
    sprayRanX = randint(-radius, radius)
    sprayRanY = randint(-radius, radius)
    dotDist = sqrt(((x + sprayRanX) - x) ** 2 + ((y + sprayRanY) - y) ** 2)
    # If the distance between the randomly generated point and the center is less than the radius, draw a dot at that point
    # this will result in a circular "spray can"
    if dotDist <= radius:
        draw.circle(surface, color, (x + sprayRanX, y + sprayRanY), 1)

# Brush Tool
def brushTool(surface, color, ox, oy, x, y, size):
    # This uses similiar triangle concepts to draw circles between the old mouse position and the new mouse position
    # this will result in a very smooth line
    # the thickness of the brush tool is determined by the size of the circles drawn
    draw.circle(surface,color,(x,y),size)
    draw.circle(surface,color,(ox,oy),size)
    dx = ox - x
    dy = oy - y
    dist = sqrt(dx**2+dy**2)
    for d in range(1,int(dist)):
        dotX = d*dx/dist + x    # This is the x coordinate of the center of the circle
        dotY = d*dy/dist + y    # This is the y coordinate of the center of the circle
        draw.circle(surface,color,(int(dotX),int(dotY)),size)

# Eraser Tool
def eraserTool(surface, ox, oy, x, y, size, custom, userBackground):

    if custom == False:
        # if the user is not using a custom background (that means the background is the default white), then 
        # the eraser tool is just a brush tool but drawing white so it appears to be "erasing" stuff
        draw.circle(surface,WHITE,(x,y),size)
        draw.circle(surface,WHITE,(ox, oy),size)
        dx = ox - x
        dy = oy - y
        dist = sqrt(dx**2+dy**2)
        for d in range(1,int(dist)):
            dotX = d*dx/dist + x
            dotY = d*dy/dist + y
            draw.circle(surface,WHITE,(int(dotX),int(dotY)),size)
    if custom:
        # If the user IS using a custom canvas background, then the eraser tool is a little different
        if x - size > 0 and y - size > 0 and x + size < 960 and y + size < 685:
            if ox - size > 0 and oy - size > 0 and ox + size < 960 and oy + size < 685:
                # Given that it is within the canvas, this eraser tool will take the section that matches the position that the 
                # user's mouse is on and will copy and paste that section onto the canvas
                # The pasting part is done by using the brush tool concept but instead of drawing circles, it is blitting on
                # sections of the user's background                
                sectionA = userBackground.subsurface((ox-size,oy-size,size*2,size*2))
                sectionB = userBackground.subsurface((x-size,y-size,size*2,size*2))
                surface.blit(sectionA,(ox-size,oy-size))
                surface.blit(sectionB,(x-size,y-size))
                dx = ox - x
                dy = oy - y
                dist = sqrt(dx**2+dy**2)
                for d in range(1,int(dist)):
                    dotX = d*dx/dist + x
                    dotY = d*dy/dist + y
                    sectionC = userBackground.subsurface((int(dotX)-size,int(dotY)-size,size*2,size*2))
                    surface.blit(sectionC,(int(dotX)-size,int(dotY)-size))


# Eye dropper tool
def dropperTool(surface, x, y):
    # takes the RGBA value of the pixel that the user clicked on and returns it
    color = surface.get_at((x, y))
    return color


# Line Tool
def lineTool(surface, ox, oy, x, y, color, size, canvasCapture):
    # ox and oy in this case are the variables shapeOX and shapeOY defined in main.py
    # So this function will first repeatedly blit a capture of the canvas from when the mouse button first goes down
    # and will draw lines from the the point (shapeOX, shapeOY) [where the mouse was first pressed
    # with the line tool selected] to the current location of the user's mouse until the mouse button is released

    surface.blit(canvasCapture, (0,0))
    draw.line(surface, color, (ox, oy),(x, y), size)


# Rectangle Tool
def rectangleTool(surface, ox, oy, x, y, color, size, canvasCapture, fill):
    if fill:
    # If the user toggled the fill button to on:
    
        surface.blit(canvasCapture, (0,0))
        rectWidth = x - ox
        rectHeight = y - oy


        if rectWidth > 0 and rectHeight > 0:
            # If user stretched the rectangle to quadrant 1
            rectWidth = sqrt(rectWidth ** 2)    # Over here, this is taking the absolute value of delta x and delta y
            rectHeight = sqrt(rectHeight ** 2)  # even though this is not necessary since the width and height will be positive anyways
            draw.rect(surface, color, (ox, oy, rectWidth, rectHeight)) # Drawing from from the old mouse position to the new mouse position

        if rectWidth < 0 and rectHeight > 0:
            # If user is drawing in quadrant 2
            rectWidth = sqrt(rectWidth ** 2)
            rectHeight = sqrt(rectHeight ** 2)
            # Instead of draw from ox, I am drawing from ox - rectWidth because since the width of the rectangle cannot be negative, I will just start where the rectangle is 
            # supposed to end 
            draw.rect(surface, color, (ox - rectWidth, oy, rectWidth, rectHeight))

        if rectWidth > 0 and rectHeight < 0:
            # Quadrant 4. Same concept.
            rectWidth = sqrt(rectWidth ** 2)
            rectHeight = sqrt(rectHeight ** 2)
            draw.rect(surface, color, (ox, oy - rectHeight, rectWidth, rectHeight))
            
        if rectWidth < 0 and rectHeight < 0:
            # Quadrant 3. 
            rectWidth = sqrt(rectWidth ** 2)
            rectHeight = sqrt(rectHeight ** 2)
            draw.rect(surface, color, (ox- rectWidth, oy - rectHeight, rectWidth, rectHeight))

    if fill == False:
    # The following is basically the same as the filled one but just with an extra parameter 
    # while drawing rect (the outline thickness)
        surface.blit(canvasCapture, (0,0))
        rectWidth = x - ox
        rectHeight = y - oy

        if rectWidth > 0 and rectHeight > 0:
            rectWidth = sqrt(rectWidth ** 2)
            rectHeight = sqrt(rectHeight ** 2)

            draw.rect(surface, color, (ox, oy, rectWidth, rectHeight), size)
        if rectWidth < 0 and rectHeight > 0:
            rectWidth = sqrt(rectWidth ** 2)
            rectHeight = sqrt(rectHeight ** 2)
            draw.rect(surface, color, (ox - rectWidth, oy, rectWidth, rectHeight), size)

        if rectWidth > 0 and rectHeight < 0:
            rectWidth = sqrt(rectWidth ** 2)
            rectHeight = sqrt(rectHeight ** 2)
            draw.rect(surface, color, (ox, oy - rectHeight, rectWidth, rectHeight), size)

        if rectWidth < 0 and rectHeight < 0:
            rectWidth = sqrt(rectWidth ** 2)
            rectHeight = sqrt(rectHeight ** 2)
            draw.rect(surface, color, (ox- rectWidth, oy - rectHeight, rectWidth, rectHeight), size)

# Ellipse Tool
def circleTool(surface, ox, oy, x, y, color, size, canvasCapture, fill):
    # ellipse tool. I used the exact same code as the rectangle tool but just for an ellipse instead. 
    if fill == True:
        surface.blit(canvasCapture, (0,0))
        circleWidth = x - ox
        circleHeight = y - oy

        if circleWidth > 0 and circleHeight > 0:
            circleWidth = sqrt(circleWidth ** 2)
            circleHeight = sqrt(circleHeight ** 2)
            draw.ellipse(surface, color, (ox, oy, circleWidth, circleHeight))

        if circleWidth < 0 and circleHeight > 0:
            circleWidth = sqrt(circleWidth ** 2)
            circleHeight = sqrt(circleHeight ** 2)
            draw.ellipse(surface, color, (ox - circleWidth, oy, circleWidth, circleHeight))

        if circleWidth > 0 and circleHeight < 0:
            circleWidth = sqrt(circleWidth ** 2)
            circleHeight = sqrt(circleHeight ** 2)
            draw.ellipse(surface, color, (ox, oy - circleHeight, circleWidth, circleHeight))

        if circleWidth < 0 and circleHeight < 0:
            circleWidth = sqrt(circleWidth ** 2)
            circleHeight = sqrt(circleHeight ** 2)
            draw.ellipse(surface, color, (ox- circleWidth, oy - circleHeight, circleWidth, circleHeight))

    if fill == False:
        surface.blit(canvasCapture, (0,0))
        circleWidth = x - ox
        circleHeight = y - oy

        if circleWidth > 0 and circleHeight > 0:
            circleWidth = sqrt(circleWidth ** 2)
            circleHeight = sqrt(circleHeight ** 2)
            draw.ellipse(surface, color, (ox, oy, circleWidth, circleHeight), size)

        if circleWidth < 0 and circleHeight > 0:
            circleWidth = sqrt(circleWidth ** 2)
            circleHeight = sqrt(circleHeight ** 2)
            draw.ellipse(surface, color, (ox - circleWidth, oy, circleWidth, circleHeight), size)

        if circleWidth > 0 and circleHeight < 0:
            circleWidth = sqrt(circleWidth ** 2)
            circleHeight = sqrt(circleHeight ** 2)
            draw.ellipse(surface, color, (ox, oy - circleHeight, circleWidth, circleHeight), size)

        if circleWidth < 0 and circleHeight < 0:
            circleWidth = sqrt(circleWidth ** 2)
            circleHeight = sqrt(circleHeight ** 2)
            draw.ellipse(surface, color, (ox- circleWidth, oy - circleHeight, circleWidth, circleHeight), size)


# Calligraphy Pen Tool
def calligraphyTool(surface, ox, oy, x, y, color, size):
    # All that is happening here is that instead of drawing a singular line, I am drawing multiple lines ({size} amount of lines to be exact) stacked together 
    # to create the calligraphy pen effect.
    for i in range(size):
        draw.line(surface, color, (ox, oy+i),(x, y+i), 2)



# Higlighter Tool
def highlighterTool(surface, color, ox, oy, x, y, size):
    # Highlighter tool. I stole Mr.McKenzie's code and implented it into mine :)
    brushHead = Surface((size*2, size*2), SRCALPHA) # Making the surface for the alpha tool. It will be twice the size of the tool size. 

    # The function for the following is that I am splitting the RGBA values of the currently selected colors into 
    # 4 individual variables so that I can change the alpha value of the color.
    R, G, B, A = color
    alphaCol = R, G, B, 3
    # Drawing a circle with the translucent color onto the brushHead surface
    draw.circle(brushHead, alphaCol, (size, size), size)    # Will be the same size as the tool size

    # If the mouse is moving (this is so that there aren't any of those weird colliding spots when drawing the line)
    if x != ox or y != oy:

        # Used the same concept as the brush tool but instead of drawing circles, im blitting the brushHead surface with the alpha circles 
        # between the old mouse position and the current.
        surface.blit(brushHead, (x-size, y-size))
        surface.blit(brushHead, (ox-size, oy-size))
        dx = ox - x
        dy = oy - y
        dist = sqrt(dx**2+dy**2)
        for d in range(1,int(dist)):
            dotX = d*dx/dist + x
            dotY = d*dy/dist + y
            surface.blit(brushHead, (dotX-size, dotY-size))


# Bucket Tool
def bucketTool(surface, x, y, color):
    # Flood fill tool. 
    # I used PixelArray for that sweet 40% efficiency boost.
    surfaceLocation = PixelArray(surface)
    targetColor = surfaceLocation[x, y]    # The color that will be checked first is the mouse click position on the canvas 
    if targetColor != color:    # If the target color is not the same as the color that the user wants to fill in, it will start the flood fill.
        toFill = []             # Here I made 2 lists and a set (more speed!) to keep track of the pixels that are going to be filled at the end of the loop, 
        toCheck = [(x, y)]      # the pixels that I need to check, and the pixels that were already checked.
        checked = set()
        while toCheck != []:    # While ther are still pixels to check:
            x, y = toCheck.pop()    # Pop the last pixel from the toCheck list and check it.
            if surfaceLocation[x, y] == targetColor:    # If the pixel is the same color as the orginal target color, add it to the toFill list and the checked set.
                toFill.append((x, y))
                checked.add((x, y))
                # Check the pixels around the current pixel that is being checked to see if they are the same color as the target color. 
                # If they are, add them to the toCheck list. But only if they weren't already checked before. 
                if x+1 < surface.get_width() and (x+1, y) not in checked:   
                    toCheck.append((x+1, y))
                if x-1 >= 0 and (x-1, y) not in checked:
                    toCheck.append((x-1, y))
                if y+1 < surface.get_height() and (x, y+1) not in checked:
                    toCheck.append((x, y+1))
                if y-1 >= 0 and (x, y-1) not in checked:
                    toCheck.append((x, y-1))

        for x, y in toFill:
            # After all the checking is done, change the color of all the pixels in the toFill list to the color that the user wants.
            surfaceLocation[x, y] = color






# Clear Canvas
def clearCanva(surface, custom, userBackground):
    # Very simple function. If the user has the default background, make canvas entirely white again.
    # If user has a custom background, blit the original background onto the canvas over everything.
    if custom == False:
        surface.fill(WHITE)
    if custom:
        surface.blit(userBackground, (0,0))

