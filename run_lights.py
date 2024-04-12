import numpy as np
import tensorflow as tf
import serial


arduino = serial.Serial('COM3', 115200)  # Adjust COM port and baud rate as needed
num = 0
array = np.array([])

while True:
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
        transformed = np.fft.rfft(array).real
        array = np.array([])
        num = 0
        print(tf.shape(transformed))
        transformed = tf.convert_to_tensor(transformed, dtype=tf.float32)
        transformed = tf.reshape(transformed, [1, 51, 1])
        model = tf.keras.models.load_model('model.keras')
        prediction = model.predict(transformed)
        prediction = tf.nn.softmax(prediction).numpy()
        prediction = str(np.argmax(prediction, 1)[0]).encode('utf-8')
        print(prediction)
        arduino.write(prediction)
    
    