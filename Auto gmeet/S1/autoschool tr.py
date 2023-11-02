import pyautogui as pg
import time as qb
import sys
import random

# one hour wait
for remaining in range(5400, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    qb.sleep(1)

sys.stdout.write("\rComplete!            \n")

# homeroom join
pg.moveTo(149,53,2)
pg.click()
qb.sleep(2)
pg.write('https://meet.google.com/', interval=0.10)
qb.sleep(2)
pg.press('enter')
pg.moveTo(1888,133,2)
pg.click()
pg.moveTo(1619,534,2)
pg.click()
qb.sleep(2)
pg.moveTo(1319,595,1)
pg.click()
qb.sleep(9)
pg.moveTo(765,765,2)
pg.click()
pg.moveTo(677,765,2)
pg.click()
pg.moveTo(1263,613,2)
pg.click()
# wait 10 minutes in hr until 12:40 pm
for remaining in range(600, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    qb.sleep(1)

sys.stdout.write("\rComplete!            \n")

# leave hr and wait 27 minutes until 1:07 pm
pg.moveTo(978,995,2)
pg.click()
for remaining in range(1620, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    qb.sleep(1)

sys.stdout.write("\rComplete!            \n")

# second class join (civics)
pg.moveTo(149,53,2)
pg.click()
qb.sleep(2)
pg.write('https://meet.google.com/lookup/a5ksw66kat?authuser=3&hs=179', interval=0.10)
qb.sleep(2)
pg.press('enter')
qb.sleep(9)
pg.moveTo(765,765,2)
pg.click()
pg.moveTo(677,765,2)
pg.click()
pg.moveTo(1263,613,2)
pg.click()
# wait in second class for 53 minutes until 2:00 pm
for remaining in range(3180, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    qb.sleep(1)

sys.stdout.write("\rComplete!            \n")

# leave second class and wait 5 minutes until 2:05 pm
pg.moveTo(978,995,2)
pg.click()
for remaining in range(300, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    qb.sleep(1)

sys.stdout.write("\rComplete!            \n")

# third class join (scimathrw Mckinstry)
pg.moveTo(149,53,2)
pg.click()
qb.sleep(2)
pg.write('https://meet.google.com/wtk-sowq-qog?pli=1&authuser=3', interval=0.01)
pg.press('enter')
qb.sleep(9)
pg.moveTo(765,765,2)
pg.click()
pg.moveTo(677,765,2)
pg.click()
pg.moveTo(1263,613,2)
pg.click()
# third class talk
qb.sleep(2)
# random statement variable
state=['I dont need any help with my class but thank you','I think I should be good for all my classes','Im not caught up at the moment but I will continue to work']
x=random.choice(state)
# open chat
pg.moveTo(1674,119,2)
pg.click()
qb.sleep(2)
pg.write( x, interval=0.01)
qb.sleep (2)
pg.press('enter')
for remaining in range(30, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    qb.sleep(1)

sys.stdout.write("\rComplete!            \n")

# leave call
pg.moveTo(781,992,2)
pg.click()
