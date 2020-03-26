from ggame import App, Sprite, ImageAsset, Frame, CircleAsset, Sprite
from ggame import Color, LineStyle, RectangleAsset
import math
from time import time
import random

#taken from https://github.com/Runpython-IntroProgramming/Course-Syllabus/wiki/Displaying-Graphics

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

def makeBackground(color,app):
    #create some instances of Color(color, alpha)
    #for more info read https://ggame.readthedocs.io/en/latest/ggameapi.html#color
    
    # Define a line style that is a thin (1 pixel) wide black line
    thinline = LineStyle(0, color)
    
    #create an instance of RectangleAsset(width, height, line=LineStyle(1, BLACK), fill=BLACK)
    #for more info read https://ggame.readthedocs.io/en/latest/ggameapi.html#rectangleasset
    
    # Now display a rectangle
    rectangle = RectangleAsset(app.width, app.height, thinline, color)
    return Sprite(rectangle)

def addStars(num,app):
    #create an imageAsset 
    #ImageAsset(url, frame=None, qty=1, direction='horizontal', margin=0)
    #https://ggame.readthedocs.io/en/latest/ggameapi.html#imageasset
    starImage = ImageAsset("star.png")
    
    #the list of stars to return at the end
    starList = []
    for i in range(num):
        #create a random position using randrange
        #https://docs.python.org/3/library/random.html#functions-for-integers
        randomPosition = (random.randrange(app.width),random.randrange(app.height))
        
        #create a sprite from the image asset
        #https://ggame.readthedocs.io/en/latest/ggameapi.html#sprite
        #Sprite(asset, pos=(0, 0), edgedef=None)
        starSprite = Sprite(starImage,randomPosition)
        starList.append(starSprite)
    return starList
        
if __name__ == "__main__":
    # execute only if run as a script
    
    #load the game
    myapp = App()

    makeBackground(black,myapp)
    addStars(50,myapp)
    
    #run the game
    myapp.run()
