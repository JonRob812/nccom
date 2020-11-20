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

script_name = os.path.basename(__file__)
settings = script_name_to_settings_pattern.search(script_name).groupdict()


def get_port():
    prt = serial.Serial()
    prt.port = settings['port']
    prt.baud = int(settings['baud'])
    prt.bytesize = serial.SEVENBITS
    prt.parity = serial.PARITY_EVEN
    prt.stopbits = 2
    prt.xonxoff = True
    return prt


def prompt_exit():
    input('any input to close\n')
    exit()


def send_file():
    try:
        send_data = open(sys.argv[1], 'r')
        send_data = send_data.read().encode()
    except:
        print('file read error')
        prompt_exit()

    print(f'begin transmission to {settings["machine"]}, this will close if complete')
    try:
        port = get_port()
        port.write(send_data)
        port.close()
    except:
        print('transmission failed')
        prompt_exit()


def save_file():
    save_name = input('input save name: ')
    if len(save_name) < 1:
        print('invalid')
        save_file()
    else:
        try:
            port = get_port()
            incoming = port.read_until(b'\x14')
            print(incoming)
        except Exception as ex:
            print('error', ex)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        save_file()

    else:
        send_file()
