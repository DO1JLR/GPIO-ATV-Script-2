#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# https://github.com/DO1JLR/GPIO-ATV-Script-2
#
# Licence: MIT License
#
from sys import argv         # fuer die kommandozeilenargumente
from time import time, sleep # fuer zeit und so...
src = "https://github.com/DO1JLR/GPIO.ATV-Script-2"
try:
    import RPi.GPIO as GPIO  # raspi gpio-pins
except:
    print("\nFehler beim Laden des GPIO Moduls.\n\tLaueft dieses Script auf einem Raspberry Pi 3?\n\tIst Python3 installiert?\n\tSind die GPIOs vorhanden?\n")
    print("\nWenn du der meinung bist, dass es sich hierbei um\n einen Fehler handelt, dann sag bescheid unter\n '" + src + "/issues'!\n\tDanke!\n\n")
    exit()
#
# Globale Variabeln:
#
version = "0.1"
debug = False
s = 30 # Wie lange soll sich das Script einegebene Werte merken
#
# GPIO Pin belegung: https://pinout.xyz/
#
# Erstmal definieren welche Pins Input sind...
senden = {"37": 0}
reset = {"35": 0}
dtmf_in = {
    "33": 0,
    "31": 0, 
    "29": 0, 
    "27": 0
}
# 
# Fuer jeden Output die Gruppe der Input-Pins:
#
dtmf_out = {
    "11": 0, 
    "13": 0, 
    "15": 0,
    "16": 0,
    "18": 0,
    "19": 0,
    "21": 0,
    "23": 0
}
#
# Komandozeilenargumente Auslesen
#
for i in argv:
    if i in ["--help", "-h", "/h", "/help", "?", "h"]:
        print("\nMoegliche Befehle:\n -h\t--help   \tZeige diese Hilfe")
        print(" -v\t--version \tZeigt die Version dieser Software")
        print("\t--debug   \tAktiviere den Debugging Modus")
        exit()
    elif i in ["-v", "--version"]:
        print("Version:\t{0}\n".format(version))
        print("Dieser Code wird verwaltet via GitHub unter:\n'" + src + "'.\n\nIst etwas kaputt?\nDann reparier es doch oder sag zumindest beschei unter '" + src + "/issues'")
        exit()
    elif i == "--debug":
        debug = True
        print("\n[I] Aktiviere den Debugging-Modus!\n\n")

#
# Den eigendlichen Code des Programmes:
#
def main():
    #
    # GPIOs einstellen
    # https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
    #
    GPIO.setwarnings(False) #  Keine nerfigen sinnlosen Meldungen
    GPIO.setmode(GPIO.BOARD) # Nutze BOARD nicht BCM.
    if debug: print("[I] Einrichten der Raspberry Pi GPIOs:")
    for key, value in senden():
        if debug: print("    Senden Input: " + str(key) )
        GPIO.setup(int(key), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    for key, value in reset():
        if debug: print("    Reset Input: " + str(key) )
        GPIO.setup(int(key), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    for key, value in dtmf_in():
        if debug: print("    DTMF Input: " + str(key) )
        GPIO.setup(int(key), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    for key, value in dtmf_out:
        if debug: print("    Output: " + str(key) )
        GPIO.setup(key, GPIO.OUT)
                
    if debug: print("[I] Konfigurien der GPIOs abgeschlossen\n[I] Starte 'while True'-Schleife\n")
    while True:
        sleep(0.23)
        #
        # ermittle GPIO Input Signale
        #  ...und schreibe sie in die RX Liste!
        #
        if debug: print("\n[O]  Liste mit den Eingangssignalen:")
        i = 0
        for key, value in inputpin.items():
            inputpin[str(key)] = GPIO.input(int(key))
            if debug: print("GPIO Input: " + str(key) + " = " + str(value))

        #
        # Schalte GPIO Output
        #
        if debug: print("\n[O]  Folgendes wird geschaltet:")
        for key in output:
            makeOutput = True
            for i in outputpin[str(key)]:
                a = (inputpin[str(i)])
                if debug: print("     Pin: " + str(key) + " prüfe Pin " + str(i) + " er ist auf " + str(a))
                if a == False:
                    makeOutput = False
            if makeOutput == True:
                GPIO.output(int(key), GPIO.HIGH)
                if debug: print("[I]  Setze den Output")
            else:
                GPIO.output(int(key), GPIO.LOW)
                if debug: print("[-]  Kein Output")



        

#
# main() ausführen
#
try:
    main()
except KeyboardInterrupt:
    if debug: print("\n[I] KeyboardInterrupt erkannt\n")
    print("\n\nProgramm wird abgebrochen!\n\n Auf Wiedersehen...\n\n")
    GPIO.cleanup()
    exit()

