import RPi.GPIO as GPIO
import time, datetime,sqlite3

SENSORS = {'hallway':7 ,'kitchen':11,'landing':13}

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

def test_pir(NAME,PIR_PIN):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIR_PIN, GPIO.IN)
    if GPIO.input(PIR_PIN):
        print "Motion Detected!"
        #c.execute('''
        #    INSERT INTO senor (SENSOR,STATUS)
        #    VALUES ('''+NAME+''',1);
        #    ''')
        time.sleep(1)

conn = sqlite3.connect('../housealarm.db')

c = conn.cursor()

c.execute ('''
CREATE TABLE IF NOT EXISTS `sensor` (
    `SENSOR`	TEXT NOT NULL PRIMARY KEY UNIQUE,
    `STATUS`	INTEGER NOT NULL
);
''')




try:
    print "PIR Module Test (CTRL+C to exit)"
    time.sleep(2)
    print "Ready"
    while True:
        for SENSOR, PIN in SENSORS.iteritems():
             print SENSOR +' on pin',PIN
             test_pir(SENSOR, PIN)
        time.sleep(1)
except KeyboardInterrupt:
               print "Quit"
               GPIO.cleanup()
