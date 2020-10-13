import tensorflow as tf
import os
import time

data = tf.constant([[1,1],[0,0],[2,0],[2,1],[3,0],[0,4],[5,6],[0,10]])
label = tf.constant([1,0,0,1,0,0,1,0])

model = tf.keras.Sequential(
    [
        tf.keras.Input(shape=(2,)),
        tf.keras.layers.Dense(20,activation="relu"),
        tf.keras.layers.Dense(2,activation="softmax")
    ]
)

print(model.summary())

model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=['accuracy'])


model.fit(data,label,batch_size=2, epochs=5)

ts = int(time.time())
file_path = "./saved_models/{}".format(ts)
# tf.saved_model.save(model, os.path.join('.','linear_model/1/'))
model.save(file_path,save_format="tf")