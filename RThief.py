import libtcodpy as lcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
FPS = 30

lcod.console_set_custom_font('arial10x10.png' , lcod.FONT_LAYOUT_TCOD | lcod.FONT_TYPE_GREYSCALE)


lcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT,'Rogue, more like Thief',False)

#prossima riga usata solo in real time 
lcod.sys_set_fps(FPS)

playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

def checkKeys():
    global playerx, playery
    #key = lcod.console_check_for_keypress()
    key = lcod.console_wait_for_keypress(True)
    if key.vk == lcod.KEY_ENTER and key.lalt:
        # alt+enter to toggle fullscreen
        lcod.console_set_fullscreen(not lcod.console_is_fullscreen()) # console.is_fullscreen return true if fullscreen, false otherwise
    elif key.vk == lcod.KEY_ESCAPE:
        return True
    
    # movement keys
    if lcod.console_is_key_pressed(lcod.KEY_UP):
        playery -= 1
    elif lcod.console_is_key_pressed(lcod.KEY_DOWN):
        playery += 1
    elif lcod.console_is_key_pressed(lcod.KEY_LEFT):
        playerx -= 1
    elif lcod.console_is_key_pressed(lcod.KEY_RIGHT):
        playerx += 1

while not lcod.console_is_window_closed():
    lcod.console_set_default_foreground(0, lcod.white)
    lcod.console_put_char(0, playerx, playery, '@', lcod.BKGND_NONE)
    
    lcod.console_flush()
    
    lcod.console_put_char(0, playerx, playery, ' ', lcod.BKGND_NONE)
    if checkKeys():
        break