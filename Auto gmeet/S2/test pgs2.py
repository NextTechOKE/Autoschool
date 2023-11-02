import pyautogui as pg
import time as qb
import sys
import random
import datetime 
import pytz
import pause, datetime

#dt = datetime.datetime(2021, 3, 19, 20, 20, 34, 383752)
#pause.until(dt)


today = datetime.datetime.now()

sleep = (datetime.datetime(today.year, today.month, today.day, 20, 31, 0) - today).seconds
print('Waiting for ' + str(datetime.timedelta(seconds=sleep)))
qb.sleep(sleep)


pg.moveTo(149,53,2)
