import serial

ser = serial.Serial(port = 'COM5', baudrate = 115200, bytesize = 8, parity = serial.PARITY_NONE, stopbits = 1, xonxoff=False)

while True:
    data = ser.readline()
    print(data)
    print(data.decode())            #decode bytes to a string
