from ggame import App, Sprite, ImageAsset, Frame, CircleAsset
from ggame import Color, LineStyle, RectangleAsset
import math
from time import time

#load the game
myapp = App()

#taken from https://github.com/Runpython-IntroProgramming/Course-Syllabus/wiki/Displaying-Graphics

def makeBackground():
    #create some instances of Color(color, alpha)
    #for more info read https://ggame.readthedocs.io/en/latest/ggameapi.html#color
    
    # Three primary colors with no transparency (alpha = 1.0)
    red = Color(0xff0000, 1.0)
    green = Color(0x00ff00, 1.0)
    blue = Color(0x0000ff, 1.0)
    black = Color(0x000000, 1.0)
    
    # Define a line style that is a thin (1 pixel) wide black line
    thinline = LineStyle(1, black)
    
    #create an instance of RectangleAsset(width, height, line=LineStyle(1, BLACK), fill=BLACK)
    #for more info read https://ggame.readthedocs.io/en/latest/ggameapi.html#rectangleasset
    
    # Now display a rectangle
    rectangle = RectangleAsset(myapp.width, myapp.height, thinline, black)
    Sprite(rectangle)

makeBackground()
#run the game
myapp.run()