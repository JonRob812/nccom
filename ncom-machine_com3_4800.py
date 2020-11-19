import sys
import os
import re
import serial
"""
the script name drive this show:

ex: ncom-Toyoda_com2_1200.py  will send to com2 at a buadrate of 1200

to use: drop a file to send or run from cli and supply the file as first arg

"""
script_name_to_settings_pattern = re.compile(r'\w*-(?P<machine>\w*?)_(?P<port>\w*?)_(?P<baud>\d*).py')

script_name = os.path.basename(__file__)
settings = script_name_to_settings_pattern.search(script_name).groupdict()


def prompt_exit():
    global x
    x = input('any input to close')
    exit()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('no file to send')
        x = input('any key to close')
    else:
        try:
            send_data = open(sys.argv[1], 'r')
            send_data = send_data.read().encode()
        except:
            print('file read error')
            prompt_exit()

        with serial.Serial(settings['port'],
                           int(settings['baud']),
                           serial.SEVENBITS,
                           serial.PARITY_EVEN, 2, None, True) as port:
            print(f'begin transmission to {settings["name"]}, this will close if complete')
            try:
                port.write(send_data)
            except:
                print('transmission failed')
                prompt_exit()



