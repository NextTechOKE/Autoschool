import pyautogui as pg
import time as qb
import sys
import random
import datetime 
import pytz
import pause

# wait until 12:30 pm est
today = datetime.datetime.now()

sleep = (datetime.datetime(today.year, today.month, today.day, 12, 30, 0) - today).seconds
print('Waiting for ' + str(datetime.timedelta(seconds=sleep)))
qb.sleep(sleep)

# homeroom join
pg.moveTo(149,53,2)
pg.click()
qb.sleep(2)
pg.write('https://meet.google.com/krz-mrcq-yqo?authuser=5', interval=0.10)
qb.sleep(2)
pg.press('enter')
qb.sleep(9)
pg.moveTo(770,727,2)
pg.click()
pg.moveTo(695,734,2)
pg.click()
pg.moveTo(1263,613,2)
pg.click()

# wait 10 minutes (600) in hr until 12:40 pm
for remaining in range(600, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    qb.sleep(1)

sys.stdout.write("\rComplete!            \n")

# leave hr and wait 27 minutes (1620) until 1:07 pm
pg.moveTo(978,995,2)
pg.click()
for remaining in range(1620, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    qb.sleep(1)

sys.stdout.write("\rComplete!            \n")

# second class join (econ)
pg.moveTo(149,53,2)
pg.click()
qb.sleep(2)
pg.write('https://meet.google.com/vid-isac-bqc?authuser=5', interval=0.10)
qb.sleep(2)
pg.press('enter')
qb.sleep(9)
pg.moveTo(770,727,2)
pg.click()
pg.moveTo(695,734,2)
pg.click()
pg.moveTo(1263,613,2)
pg.click()
# wait in second class for 53 minutes (3180) until 2:00 pm
for remaining in range(3180, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    qb.sleep(1)

sys.stdout.write("\rComplete!            \n")

# leave second class and wait 5 minutes (300) until 2:05 pm
pg.moveTo(978,995,2)
pg.click()
for remaining in range(300, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    qb.sleep(1)

sys.stdout.write("\rComplete!            \n")

# third class join (stats Mckinstry)
pg.moveTo(149,53,2)
pg.click()
qb.sleep(2)
pg.write('phdr', interval=0.01)
pg.press('enter')
qb.sleep(9)
pg.moveTo(770,727,2)
pg.click()
pg.moveTo(695,734,2)
pg.click()
pg.moveTo(1263,613,2)
pg.click()
# third class 10 minute (600) wait
qb.sleep(600)

# leave call
pg.moveTo(781,992,2)
pg.click()
