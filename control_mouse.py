import serial
import mouse
import math

def data_handler(tokens):
	global click

	sw   = int(tokens[0])
	x    = int(tokens[1])
	y    = int(tokens[2])
	sens = int(tokens[3])
	
	# Sensitivity
	sens = math.floor(sens / 100) + 1
	print("Sensitivity:", sens)

	# Switch Click
	if sw == 1 and click == 0:
		mouse.click()
	click = sw

	MIDDLE_JOYSTICK = 505
	# X movement
	x = ((x - MIDDLE_JOYSTICK) / MIDDLE_JOYSTICK) * sens
	
	# Y movement
	y = ((y - MIDDLE_JOYSTICK) / MIDDLE_JOYSTICK) * sens

	mouse.move(x, y, False)

def read_serial(ser):
	string = ""
	while True:
		for c in ser.read():
			if chr(c) == ";":
				data_handler(string.split(':'))
				string = ""
			else:
				string += chr(c)

def main():
	ser = serial.Serial('COM3', 9600)
	if ser.isOpen():
		print("Connected to: " + ser.portstr)
	else:
		return

	read_serial(ser)
	ser.close()

if __name__ == "__main__":
	main()
