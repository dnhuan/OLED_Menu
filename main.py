#!/usr/bin/python
# -*- coding:utf-8 -*-\
from __future__ import print_function

import os
import signal
import time
import configparser

import config
import utils
import pimodules as pim
import displayGUI

import RPi.GPIO as GPIO

## GPIO define
KEY_UP_PIN     = config.KEY_UP_PIN
KEY_DOWN_PIN   = config.KEY_DOWN_PIN
KEY_LEFT_PIN   = config.KEY_LEFT_PIN
KEY_RIGHT_PIN  = config.KEY_RIGHT_PIN
KEY_PRESS_PIN  = config.KEY_PRESS_PIN

KEY1_PIN       = config.KEY1_PIN
KEY2_PIN       = config.KEY2_PIN
KEY3_PIN       = config.KEY3_PIN

## Init GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up

GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up


## Handle keypresses
def KEY_UP(channel):
    # pim.key_handler(channel)
    while GPIO.input(KEY_UP_PIN) == False:
        pim.key_handler(channel)
        time.sleep(0.3)

def KEY_DOWN(channel):
    # pim.key_handler(channel)
    while GPIO.input(KEY_DOWN_PIN) == False:
        pim.key_handler(channel)
        time.sleep(0.3)

def KEY_LEFT(channel):
    # pim.key_handler(channel)
    while GPIO.input(KEY_LEFT_PIN) == False:
        pim.key_handler(channel)
        time.sleep(0.1)

def KEY_RIGHT(channel):
    # pim.key_handler(channel)
    while GPIO.input(KEY_RIGHT_PIN) == False:
        pim.key_handler(channel)
        time.sleep(0.1)

def KEY_PRESS(channel):
    pim.key_handler(channel)

def KEY1(channel):
    ## Foward / OK / ACCEPT
    pim.key_handler(channel)

def KEY2(channel):
    ## Back / Cancle
    pim.key_handler(channel)

def KEY3(channel):
    #displayGUI.contrast()
    utils.display_on_off = not utils.display_on_off

## Add interupts
GPIO.add_event_detect(KEY_UP_PIN, GPIO.FALLING, callback=KEY_UP, bouncetime=300)
GPIO.add_event_detect(KEY_DOWN_PIN, GPIO.FALLING, callback=KEY_DOWN, bouncetime=300)
GPIO.add_event_detect(KEY_LEFT_PIN, GPIO.FALLING, callback=KEY_LEFT, bouncetime=300)
GPIO.add_event_detect(KEY_RIGHT_PIN, GPIO.FALLING, callback=KEY_RIGHT, bouncetime=300)
GPIO.add_event_detect(KEY_PRESS_PIN, GPIO.FALLING, callback=KEY_PRESS, bouncetime=300)
GPIO.add_event_detect(KEY1_PIN, GPIO.FALLING, callback=KEY1, bouncetime=300)
GPIO.add_event_detect(KEY2_PIN, GPIO.FALLING, callback=KEY2, bouncetime=300)
GPIO.add_event_detect(KEY3_PIN, GPIO.FALLING, callback=KEY3, bouncetime=300)

# kill SIGs
def receiveSignal(signalNumber, frame):
    print('Received: ', signalNumber)
    config.module_exit()
    exit()

signal.signal(signal.SIGTERM, receiveSignal)

try:
    print('My PID is:', os.getpid())
    utils.init()
    pim.mainmenu(0)
    displayGUI.init()

except KeyboardInterrupt:
    print("ctrl + c:")
    config.module_exit()
    exit()