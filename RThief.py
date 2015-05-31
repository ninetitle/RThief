import libtcodpy as lcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
FPS = 30

lcod.console_set_custom_font('arial10x10.png' , lcod.FONT_LAYOUT_TCOD | lcod.FONT_TYPE_GREYSCALE)


lcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT,'Rogue, more like Thief',False)

#prossima riga usata solo in real time 
lcod.sys_set_fps(FPS)

while not lcod.console_is_window_closed():
    lcod.console_set_default_foreground(0, lcod.white)
    lcod.console_put_char(0, 1, 1, '@', lcod.BKGND_NONE)
    lcod.console_flush()
