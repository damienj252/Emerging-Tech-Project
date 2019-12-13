import numpy as np
import matplotlib.pyplot as plt
import keras as kr

from keras.datasets import mnist
from keras.models import Sequential


import constants

from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout

from keras.models import load_model

(train_imgs, train_labels), (test_imgs, test_label) = mnist.load_data()


train_imgs = train_imgs.reshape(train_imgs.shape[0], constants.img_width, constants.img_height, 1)
test_imgs = test_imgs.reshape(test_imgs.shape[0], constants.img_width, constants.img_height, 1)
input_shape = (constants.img_width, constants.img_height, 1)
train_imgs = train_imgs.astype('float32')
test_imgs = train_imgs.astype('float32')

train_imgs /= 255
test_imgs /= 255

train_labels = kr.utils.to_categorical(train_labels, constants.no_of_numbers)
test_label = kr.utils.to_categorical(test_label, constants.no_of_numbers)


model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu', input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(4, 4)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(constants.no_of_numbers, activation='softmax'))
model.compile(loss=kr.losses.categorical_crossentropy, optimizer=kr.optimizers.Adadelta(), metrics=['accuracy'])