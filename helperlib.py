import datetime, logging, os
import RPi.GPIO as GPIO

def getCurrentTime():
	now = datetime.datetime.now()
	nowFormatted = now.strftime("%H:%M:%S.%f")
	return nowFormatted

def setupLed(ioPin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ioPin,GPIO.OUT)
    GPIO.output(ioPin,False)
    
def blinkLed(ioPin):
    GPIO.output(ioPin, True)
    sleep(0.2)
    GPIO.output(ioPin, False)    

def ledOn(ioPin):
    GPIO.output(ioPin, True)

def ledOff(ioPin):
    GPIO.output(ioPin, False)

def log(message):
	logging.debug(message)
	print(message)

base = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename = base + '/timekeeper.log', format='%(asctime)s %(message)s', level=logging.DEBUG)