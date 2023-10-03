import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Pasa la tarjeta NFC cerca del lector...")
    while True:
        id, text = reader.read()
        print("Tarjeta detectada con el ID:", id)
        print("Texto en la tarjeta:", text)
finally:
    GPIO.cleanup()
