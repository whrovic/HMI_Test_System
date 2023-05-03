import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))

# import sys
# import glob
# import serial

# if (sys.platform.startswith('win')):
#     ports = ['COM%s' % (i+1) for i in range(256)]
# elif (sys.platform.startswith('linux') or sys.platform.startswith('cygwin')):
#     ports = glob.glob('/dev/tty[A-Za-z]*')
# elif (sys.platform.startswith('darwin')):
#     ports = glob.glob('/dev/tty.*')
# else:
#     raise EnvironmentError('Unsuported platform')

# result = []
# for port in ports:
#     try:
#         s = serial.Serial(port)
#         s.close()
#         result.append(port)
#     except:
#         pass

# print(result)
