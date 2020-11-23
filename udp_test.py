import sys
import os
import re
import serial
"""
the script name drive this show:

ex: Toyoda_com2_1200.py  will send to com2 at a buadrate of 1200

to use: drop a file to send or run from cli and supply the file as first arg

"""
script_name_to_settings_pattern = re.compile(r'(?P<machine>\w*?)_(?P<port>\w*?)_(?P<baud>\d*).py')

# script_name = os.path.basename(__file__)
# settings = script_name_to_settings_pattern.search(script_name).groupdict()
settings = {'port':'com4',
            'baud': 4800}


def get_port():
    prt = serial.Serial()
    prt.port = settings['port']
    prt.baudrate = int(settings['baud'])
    prt.bytesize = serial.SEVENBITS
    prt.parity = serial.PARITY_EVEN
    prt.stopbits = 2
    prt.xonxoff = True
    prt.dsrdrt = True
    prt.rtscts = True
    prt.open()
    return prt


port = get_port()

port.close()