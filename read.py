import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Rfid:
	#return uid in hexa str
	def read_uid(self):
		lector = SimpleMFRC522()
		print("      <<<<Apropi la targeta al lector>>>>")
		id = lector.read_id()
		uid = hex(id).upper()
		return uid
		
if __name__ == "__main__":
	try:
		rf = Rfid()
		print("         L'UID detectada és:"+rf.read_uid().strip("0X"))
		
	finally:
		GPIO.cleanup()

