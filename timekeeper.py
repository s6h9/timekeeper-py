#!/usr/bin/python
#coding=utf-8

import os, sys, subprocess, time, datetime, logging
from helperlib import *
from rfidlib import *
from displaylib import *

# SETUP
base = os.path.dirname(os.path.realpath(__file__))
beepFile = base + "/beep-07.wav"

# led
ledPort = 27
setupLed(ledPort)

# button
buttonPort = 8
GPIO.setup(buttonPort, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# display
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LCD_E, GPIO.OUT)
GPIO.setup(LCD_RS, GPIO.OUT)
GPIO.setup(LCD_DATA4, GPIO.OUT)
GPIO.setup(LCD_DATA5, GPIO.OUT)
GPIO.setup(LCD_DATA6, GPIO.OUT)
GPIO.setup(LCD_DATA7, GPIO.OUT)
display_init()

# MAIN
lcd_send_byte(LCD_LINE_1, LCD_CMD)
lcd_message("TimeKeeper")
lcd_send_byte(LCD_LINE_2, LCD_CMD)
lcd_message("ready!")

running = False;

try:
	# wait for button to be pushed
	while GPIO.input(buttonPort) == False:
		time.sleep(.01)
	
	# button was pressed 1 time
	startzeit = getCurrentTime()
	subprocess.Popen(["aplay", beepFile])
	log("Start " + startzeit)

	lcd_send_byte(LCD_LINE_1, LCD_CMD)
	lcd_message("START")
	lcd_send_byte(LCD_LINE_2, LCD_CMD)
	lcd_message(startzeit)
	
	running = True;

	while running:
		
		id = read_rfid()
		if id:
			# os.system('aplay ../sound/beep-07.wav')
			subprocess.Popen(["aplay", beepFile])
			now = getCurrentTime()
			ledOn(ledPort);
			lcd_clear()
			lcd_send_byte(LCD_LINE_1, LCD_CMD)
			lcd_message(id)
			lcd_send_byte(LCD_LINE_2, LCD_CMD)
			lcd_message(now)
			log("RFID " + id + " - " + now)
			time.sleep(.2)
			resetLcd()
			ledOff(ledPort)
		
		time.sleep(0.01)
			
except KeyboardInterrupt:
	clearLcd()
	log("TimeKeeper stopped.")
	sys.exit()

finally:
	clearLcd()
	GPIO.cleanup()
