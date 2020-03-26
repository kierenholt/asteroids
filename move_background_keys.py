
#do not make filenames too long, or with any spaces

from ggame import App, Sprite, ImageAsset, Frame, CircleAsset, Sprite
from ggame import Color, LineStyle, RectangleAsset
import math
from time import time
from make_a_space_backdrop import makeBackground, addStars


#taken from https://github.com/Runpython-IntroProgramming/Course-Syllabus/wiki/Displaying-Graphics

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)


if __name__ == "__main__":
    # execute only if run as a script
    
    #load the game
    myapp = App()
    
    makeBackground(black,myapp)
    addStars(50,myapp)
    
    #run the game
    myapp.run()
