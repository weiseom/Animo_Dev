import serial

ser = serial.Serial("/dev/ttyACM1",9600)

ser.flushInput()

rawValue = []

while True:
#	if (ser.inWaiting() > 0):
#		input = ser.read(1)
#		print(input)
	input_s = ser.readline()
#	input = int(input_s)
#	print(input_s)
	rawValue = input_s.split()
	print(rawValue[1])
	
	if int(rawValue[1]) < 20:
		if int(rawValue[0]) == 1:
			print("pinNum1 Danger!")
                if int(rawValue[0]) == 3:
                        print("pinNum3 Danger!")

