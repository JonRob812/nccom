import serial


ser = serial.Serial('COM3', 4800, serial.SEVENBITS, serial.PARITY_EVEN, 2, None, True,)


with open('out.nc', 'w') as file:
    done = False
    nc = []
    
    while not done:
        data = ser.read()
        if data == b'':
            pass
        else:
            nc.append(data.decode())
            file.write(data.decode())
            while not done:
                data = ser.read()
                if data == b'':
                    done = True
                    break
                else:
                    nc.append(data.decode())
                    file.write(data.decode())
                    
                    
                    
            
    print(nc)
    file.write('______')
    file.writelines(nc)
      
            
        


    
