import numpy as np

def transform(fileName):
    with open(fileName, 'r') as file:
        array = np.loadtxt(file, delimiter=',', dtype=float)
    transformedArray = np.fft.rfft(array)
    return transformedArray

def writeArray(array, fileName):
    np.savetxt(fileName, array, delimiter=',', fmt='%0.8f')
