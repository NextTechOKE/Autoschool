import pyautogui as pg
import time as qb
import sys
import random

# one hour 30 wait
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
pg.moveTo(1440,637,1)
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

# second class join (english)
pg.moveTo(149,53,2)
pg.click()
qb.sleep(2)
pg.write('https://meet.google.com/lookup/edfuaix5ij?authuser=3&hs=179', interval=0.10)
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

# progress check google form
pg.moveTo(149,53,1)
pg.click()
qb.sleep(2)
pg.write('https://docs.google.com/forms/d/e/1FAIpQLSdx485Txlho2QE2L06ZKVV9C4Ty1_igo1JzpqryJpYs1aLSDg/viewform?hr_submission=ChkIlYPPjIIBEhAIyImYr-gDEgcIybC_uOUDEAE', interval=0.10)
pg.press('enter')
qb.sleep(5)
# first and last name
pg.moveTo(823,337,1)
pg.click()
pg.write('Jace Williams', interval=0.10)
# choose elective
pg.moveTo(742,517,1)
pg.click()
pg.moveTo(729,554,1)
pg.click()
# course percentage
pg.moveTo(934,648,1)
pg.click()
pg.write('6%', interval=0.10)
# course percentage change
pg.moveTo(767,805,1)
pg.click()
pg.write('2%', interval=0.10)
# todays goal
pg.moveTo(702,950,1)
pg.click()
pg.write('complete 2 assignments', interval=0.05)
# submit form
pg.moveTo(686,1014,2)
pg.click()
# third class join (sat prep woodward)
pg.moveTo(149,53,2)
pg.click()
qb.sleep(2)
pg.write('https://meet.google.com/lookup/dm3iclko2q?authuser=3&hs=179', interval=0.10)
pg.press('enter')
qb.sleep(9)
pg.moveTo(765,765,2)
pg.click()
pg.moveTo(677,765,2)
pg.click()
pg.moveTo(1263,613,2)
pg.click()
# third class talk
for remaining in range(15, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d}".format(remaining))
    sys.stdout.flush()
    qb.sleep(1)

sys.stdout.write("\rComplete!            \n")

# open chat
pg.moveTo(1674,119,2)
pg.click()
qb.sleep(2)
pg.write('I filled out the progress check sheet and I dont need any help', interval=0.10)
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

