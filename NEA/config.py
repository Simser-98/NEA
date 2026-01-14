import pygame as pg

pg.init()
pg.font.init()

font = pg.font.SysFont('Comic Sans MS', 16)
WIN_WIDTH, WIN_HEIGHT =  1920*0.7 ,1080*0.7  #1280,720 500,500 1920,1080  2736, 1824  1600, 900
Window = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
Surface = pg.Surface((WIN_WIDTH,WIN_HEIGHT))
FPS = 500






WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 127)
BLUE_LINE = (21, 162, 232, 10)
BLUE_FILL = (0, 251, 255, 50)
GREEN_FILL = (3, 252, 11,5)
GREEN_LINE = (28, 128, 31,10)
PURPLE_LINE = (142, 7, 245,10)
PURPLE_FILL = (172, 64, 255, 45)
