import serial

# https://pyserial.readthedocs.io/en/latest/shortintro.html

ser = serial.Serial('/dev/ttyUSB0')  # open serial port
print(ser.name)         # check which port was really used

ser.write(b'hello')     # write a string
x = ser.read()          # Read one byte
s = ser.read(10)        # Read 10 bytes

# readline()

ser.close()             # close port