#! /usr/bin/python3

# nefunctional
# libraria rpi_lcd

#from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
"""
lcd = LCD()

def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
    lcd.text("ceaw", 1)
    lcd.text("Raspberry PI!",2)

    pause()

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()
"""

#aia de sus e mizerie bro, incercam altcv

lcd = LCD()

lcd.write("ceaw",1)
lcd.text("ceaw",2)
lcd.text("ceaw",3)
lcd.text("ceaw",4)
