import pyautogui as pg
import time as qb

qb.sleep (4)

pg.keyDown('ctrl')
pg.press('c')
pg.keyUp('ctrl')

pg.keyDown('ctrl')
pg.keyDown('shift')
pg.keyDown('n')

pg.keyUp('ctrl')
pg.keyUp('shift')
pg.keyUp('n')

pg.keyDown('ctrl')
pg.press('v')
pg.keyUp('ctrl')
pg.press('enter')