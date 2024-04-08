import numpy as np

def transform(tensor):

    return np.fft.rfft(tensor.eval())

def writeArray(array, fileName):
    np.savetxt(fileName, array, delimiter=',', fmt='%0.8f')
