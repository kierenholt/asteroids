
#do not make filenames too long, or with any spaces

from ggame import App, Sprite, ImageAsset, Frame, CircleAsset, Sprite
from ggame import Color, LineStyle, RectangleAsset
import math
from time import time
from make_a_space_backdrop import makeBackground, addStars


black = Color(0x000000, 1.0)

def moveSpriteDownOnKey(sprite,app,keyname):
    #bind a key to the keyboard event using listenKeyEvent(eventtype, key, callback)
    #https://ggame.readthedocs.io/en/latest/ggameapi.html#ggame.app.App.listenKeyEvent
    app.listenKeyEvent("keydown", keyname, sprite.x += 1)


if __name__ == "__main__":
    # execute only if run as a script
    
    #load the game
    myapp = App()
    
    #these functions are imported in line 8 
    makeBackground(black,myapp)
    starList = addStars(50,myapp)
    #keynames can be found here https://ggame.readthedocs.io/en/latest/ggameapi.html#ggame.event.KeyEvent.key
    for star of starList:
        moveSpriteDownOnKey(star,myapp,"up arrow")
    
    #run the game
    myapp.run()
