#!/usr/bin/python

import serial
import RPi.GPIO as GPIO
from time import sleep

# Auslesen der RFID-Transponder
def read_rfid():
    ser = serial.Serial("/dev/ttyAMA0")
    ser.baudrate = 9600
    daten = ser.read(14)
    ser.close()    
    daten = daten.replace("\x02", "" )
    daten = daten.replace("\x03", "" )
    return daten

