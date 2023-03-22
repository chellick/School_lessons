import serial
import time 

k = 1 
with serial.Serial('/dev/ttyACMO', 9600, timeout=1) as ser:
    while True:
        time.sleep(1)
        x = ser.readline()
        print(x)
        f = open('output.txt', 'a')
        f.write('\n' + str(k) + ',' + str(x)[1:].replace(" ' ", "").replace(r'\r\n', ''))
        k += 1
        