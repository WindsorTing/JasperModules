# -*- coding: utf-8-*-
import random
import re
from datetime import datetime, time
from phue import Bridge

WORDS = ["TURN", "LIGHTS", "ON","OFF"]


def handle(text, mic, profile):
	
    bridgeip = profile['bridgeip']
    b = Bridge(bridgeip)
    b.connect()
    lights = b.lights
    global message
    message = ""    

    if "on" in text.lower():
    	for l in lights:
		l.on = True
		l.brightness = 254

	message = "All Lights have been turned on"
    elif "off" in text.lower():
	for l in lights:
                l.on = False

	message = "All Lights have been turned off."
	
	now = datetime.now()
	now_time = now.time()
	if now_time >= time(21,30) and now_time <= time(02,00):
        	message += "Good Night"




    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(turn (all|the) lights)\b', text, re.IGNORECASE))

