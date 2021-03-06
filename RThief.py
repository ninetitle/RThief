import libtcodpy as lcod

from base import  Object
from MGenerator import Mappa

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
MAP_WIDTH = 80
MAP_HEIGHT = 45

#FPS = 30

lcod.console_set_custom_font('arial10x10.png' , lcod.FONT_LAYOUT_TCOD | lcod.FONT_TYPE_GREYSCALE)


lcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT,'Rogue, more like Thief',False)
con = lcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
MAPcon = lcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

#prossima riga usata solo in real time 
#lcod.sys_set_fps(FPS)

player = Object(SCREEN_WIDTH/2,SCREEN_HEIGHT/2, '@', lcod.white)

npc = Object(SCREEN_WIDTH/2 - 5,SCREEN_HEIGHT/2, '@', lcod.white)

oggetti = [npc, player]

mappa = Mappa(MAP_HEIGHT, MAP_WIDTH)


def checkKeys():
    #key = lcod.console_check_for_keypress()
    key = lcod.console_wait_for_keypress(True)
    if key.vk == lcod.KEY_ENTER and key.lalt:
        # alt+enter to toggle fullscreen
        lcod.console_set_fullscreen(not lcod.console_is_fullscreen()) # console.is_fullscreen return true if fullscreen, false otherwise
    elif key.vk == lcod.KEY_ESCAPE:
        return True
    
    # movement keys
    if lcod.console_is_key_pressed(lcod.KEY_UP):
        player.move(0, -1)
    elif lcod.console_is_key_pressed(lcod.KEY_DOWN):
        player.move(0, 1)
    elif lcod.console_is_key_pressed(lcod.KEY_LEFT):
        player.move(-1, 0)
    elif lcod.console_is_key_pressed(lcod.KEY_RIGHT):
        player.move(1, 0)

def renderActor():
    for oggetto in oggetti:
        oggetto.draw(con)
        
    lcod.console_blit(con, 0, 0,SCREEN_WIDTH,SCREEN_HEIGHT, 0, 0, 0, 1.0, 0.0 )

def RenderMap(mappa):
    global color_dark_wall 
    global color_dark_ground
    color_dark_wall = lcod.Color(0, 0, 100)
    color_dark_ground = lcod.Color(50, 50, 150)
    
    for y in range(mappa.altezza):
        for x in range(mappa.largezza):
            wall = mappa.mappa[x][y].block_sight
            if wall:
                lcod.console_set_char_background(MAPcon,x,y,color_dark_wall ,lcod.BKGND_SET)
            else:
                lcod.console_set_char_background(MAPcon,x,y,color_dark_ground,lcod.BKGND_SET)
        
        lcod.console_blit(MAPcon,0,0,SCREEN_WIDTH,SCREEN_HEIGHT,0,0,0)

while not lcod.console_is_window_closed(): # Main game loop
    lcod.console_set_default_foreground(0, lcod.white)
    RenderMap(mappa)
    renderActor()
    
    
    # source , x, y width, Height of the area to be blitted if 
    # width or height == 0 the source console value are used, dest
    # x, y destinazione, foregroundAlpha=1.0, backgroundAlpha 1.0
    lcod.console_flush()
    
    for oggetto in oggetti:
        oggetto.clear(con)
    
    exit = checkKeys()
    if exit:
        break
    