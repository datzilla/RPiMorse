import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pin = 4
GPIO.setup(pin,GPIO.OUT)

def english2morse (sentence):
	morse = dict({\
		"a" : ".- ", \
		"b" : "-... ", \
		"c" : "-.-. ", \
		"d" : "-.. ", \
                "e" : ". ", \
                "f" : "..-. ", \
                "g" : "--. ", \
                "h" : ".... ", \
                "i" : ".. ", \
                "j" : ".--- ", \
                "k" : "-.- ", \
                "l" : ".-.. ", \
                "m" : "-- ", \
                "n" : "-. ", \
                "o" : "--- ", \
                "p" : ".--. ", \
                "q" : "--.- ", \
                "r" : ".-. ", \
                "s" : "... ", \
                "t" : "- ", \
                "u" : "..- ", \
                "v" : "...- ", \
                "w" : ".-- ", \
                "x" : "-..- ", \
                "y" : "-.-- ", \
                "z" : "--.. "})

	filter = dict({\
                "{" : " ", \
                "}" : " ", \
                "(" : " ", \
                ")" : " ", \
                "\\" : " ", \
                "/" : " ", \
		"." : " ", \
		"-" : " ", \
		"," : " ", \
                "&" : " ", \
                "%" : " ", \
                "$" : " ", \
                "\#" : " ", \
                "@" : " ", \
                "!" : " ", \
                "\"" : " ", \
                "'" : " ", \
                "'" : " ", \
                "~" : " ", \
                "_" : " ", \
                "+" : " ", \
                "=" : " ", \
                "|" : " ", \
                "*" : " ", \
                "^" : " "})

	morsestring = sentence

	for symbol, value in filter.items():
		morsestring = morsestring.replace(symbol, filter[symbol])

	for alpha, value in morse.items():
		morsestring = morsestring.replace(alpha, morse[alpha])

	return morsestring

def morse2LED (pin, morse):
	for character in morse:
		if character == ".":
			#short light
			ledON (pin)
			time.sleep(500.0/1000.0)
			ledOFF (pin)
		elif character == "-":
			# long
			ledON (pin)
			time.sleep(2)
			ledOFF (pin)
		# break between code
		time.sleep (1)
	return

def ledON (pin):
	GPIO.output (pin, GPIO.HIGH)
	return

def ledOFF (pin):
	GPIO.output (4, GPIO.LOW)
	return


while (True):
	print "Enter an english sentence:"
	userinput = raw_input()
	userinput = userinput.lower()
	morsecode = english2morse (userinput)
	print "morse code: " + morsecode
	print "Emitting code. Please wait..."
	morse2LED (pin, morsecode)
