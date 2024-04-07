import serial
import numpy as np

# Open serial connection
arduino = serial.Serial('COM5', 38400)  # Adjust COM port and baud rate as needed
num = 0
filenum = 0
array = np.array([])
while filenum < 10:
    while (arduino.inWaiting()==0):
        pass
    try:  
        arduinoString = float(arduino.readline().decode('utf-8').rstrip('\r\n'))
        num+=1
        if (10<num<=110):
            array = np.append(array, arduinoString)
    except ValueError:
        continue
    if (num==110):
        np.savetxt(f'array{filenum}.csv', array, delimiter=',')
        array = np.array([])
        num = 0
        filenum+=1
# Open array0.csv and convert it into a float array
with open('array0.csv', 'r') as file:
    array0 = np.loadtxt(file, delimiter=',', dtype=float)

    
    
    
transfromedArray = np.fft.rfft(array0)

import matplotlib.pyplot as plt

# Plot the transformed array
plt.plot(np.absolute(transfromedArray.real))
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('Transformed Array')
plt.show()

# Save array as CSV


