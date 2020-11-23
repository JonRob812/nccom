import serial


ser = serial.Serial('COM4', 4800, serial.SEVENBITS, serial.PARITY_EVEN, 2, None, True,)

pgm = """%
O1212(TEST)
G0X0Z0
G1X11.134
Z-12.5
M30
%
"""

ser.write(pgm.encode())


    
