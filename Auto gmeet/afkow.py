import time as qb
import pyautogui as pg 

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