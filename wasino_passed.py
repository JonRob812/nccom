import serial
settings = {'baudrate': 4800, 'bytesize': 7, 'parity': 'E', 'stopbits': 2, 'xonxoff': True, 'dsrdtr': False, 'rtscts': True, 'timeout': None, 'write_timeout': None, 'inter_byte_timeout': None}
file = open('C:\\Users\\allan\\Desktop\\op1.nc')
data = file.read().encode()

prt = serial.Serial()
prt.port = 'com10'
prt.baudrate = 4800
prt.bytesize = serial.SEVENBITS
prt.parity = serial.PARITY_EVEN
prt.stopbits = 2
prt.xonxoff = True
prt.dsrdrt = True
prt.rtscts = True
prt.open()
print(prt.get_settings())


print(prt.write(data))
