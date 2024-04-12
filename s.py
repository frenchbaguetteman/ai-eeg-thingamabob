import tensorflow as tf
import numpy as np
import os
import pandas as pd
import glob
from tensorflow.keras import layers

files = np.sort(glob.glob("./data/*"))
label_classes = ["focus", "neutral"]
batch_size = 32

def initial_process(files, label_classes):
    for file in files:
        data = []
        labels = []
        temp = pd.read_csv(open(file, "r"))
        data.append(temp)
        for j in range(len(label_classes)):
            if label_classes[j] in file:
                labels.append(j)
        yield data, labels

data = initial_process
(files, label_classes)
dataset = tf.data.Dataset.from_generator(initial_process, args=[files, label_classes], output_signature=(tf.TensorSpec(shape=(1, 51, 1), dtype=tf.float32), tf.TensorSpec(shape=(1,), dtype=tf.int32)))
dataset = dataset.repeat(1000)

train_ds = dataset.take(int(0.8 * len(list(dataset))))
val_ds = dataset.skip(int(0.8 * len(list(dataset))))
model = tf.keras.Sequential([
    layers.Conv1D(32, 3, activation="relu", input_shape=(51,1)),
    layers.MaxPool1D(2),
    layers.Conv1D(64, 3, activation="relu"),
    layers.MaxPool1D(2),
    layers.Flatten(),
    layers.Dense(32, activation="relu"),
    layers.Dense(16, activation="relu"),
    layers.Dense(2, activation="softmax")
])
model.summary()

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(train_ds, validation_data=val_ds, epochs=10, batch_size=batch_size)
model.save("model.keras")