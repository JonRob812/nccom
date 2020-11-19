import json

wasino = {'name': 'Wasino',
          'port': 'COM3',
          'baud': 4800}

toyoda = {'name': 'Toyoda',
          'port': 'COM2',
          'baud': 1200}

A99 = {'name': 'A99',
       'port': 'COM3',
       'baud': 4800}


machines = [wasino, toyoda, A99]
print(json.dumps(wasino))
# with open('config.json', 'w') as file:
#     file.write(json.dumps(machines))

with open('config.json',) as file:
    machine_in = json.load(file)
    print(machine_in)



