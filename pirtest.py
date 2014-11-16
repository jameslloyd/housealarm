import RPi.GPIO as GPIO
import time, datetime, sqlite3

conn = sqlite3.connect('../housealarm.db')
c = conn.cursor()
c.execute (''' CREATE TABLE `log` (`id`	INTEGER PRIMARY KEY AUTOINCREMENT,`datetime` TEXT,`sensor` TEXT); ''')
GPIO.setmode(GPIO.BOARD)
SENSOR['lounge']=7
SENSOR['kitchen']=11
SENSOR['landing']=13
SENSOR['hallway']=15

PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
try:
    print "PIR Module Test (CTRL+C to exit)"
    time.sleep(2)
    print "Ready"
    while True:
        if GPIO.input(PIR_PIN):
            print "Motion Detected!"
            print datetime.datetime.now()
            time.sleep(1)
except KeyboardInterrupt:
               print "Quit"
               GPIO.cleanup()
