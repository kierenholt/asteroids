
#do not make filenames too long, or with any spaces

from ggame import App, Sprite, ImageAsset, Frame, CircleAsset, Sprite
from ggame import Color, LineStyle, RectangleAsset
import math
from time import time
from make_a_space_backdrop import makeBackground, addStars


black = Color(0x000000, 1.0)




if __name__ == "__main__":
    # execute only if run as a script
    
    #load the game
    myapp = App()
    
    #these functions are imported in line 8 
    makeBackground(black,myapp)
    addStars(50,myapp)
    
    #run the game
    myapp.run()
