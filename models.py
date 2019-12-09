# NumPy is a library for the Python programming language,
# used to adding and  supporting large, multi-dimensional arrays and matrices
import numpy as np

# Matplot lib is a two-dimensional plotting library for Python
import matplotlib.pyplot as plt

# Keras is a hign level open-source nerual-network library in Python which runs on top of TensorFlow
import keras as kr

# The MNIST database is a large database of handwritten digits that is used for training of image processing systems.
# This imports The MNIST dirctly in from the from the keras API
from keras.datasets import mnist
from keras.models import Sequential

# Imports the constants
import constants

# Importing keras dense which implemnets the operation,
# Flatten is an operation preformed in tensorflow that reshapes the tensor to have a
# shape that is equal to the number of elements contained in it.
# Conv2D converts the image into pixels and takes an n-sized window
# those features are then condensed into a feature map and the window slides
# MaxPooling2D is used for spatial data
# Dropout is a feature that stops certain neurals from training in order to
# prevent an overfitting
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout

from keras.models import load_model


# This downloads the MNIST dataset from the Keras API. The dataset has 60,000
# images and associated labels used for training and 10,000 testing images
# with associated labels. We need to seperate the dataset into two groups
# a training group and a testing group. train_imgs, train_labels,
# test_imgs and test_label.
(train_imgs, train_labels), (test_imgs, test_label) = mnist.load_data()

# We have to reshape the MNIST dataset with Keras, we will convert it from a 3d
# Array to a 4d NumPy array
# Making sure train_imgs and test_imgs are floats, so we can use decimal points
train_imgs = train_imgs.reshape(train_imgs.shape[0], constants.img_width, constants.img_height, 1)
test_imgs = test_imgs.reshape(test_imgs.shape[0], constants.img_width, constants.img_height, 1)
input_shape = (constants.img_width, constants.img_height, 1)
train_imgs = train_imgs.astype('float32')
test_imgs = train_imgs.astype('float32')

# Data is normalized when being used in a nerual network t obtain a mean close
# to 0 Normalizing the data generally speeds up learning and
# leads to faster convergence. Normalizing the RGB code by dividing it by the
# max RGB value(255)
train_imgs /= 255
test_imgs /= 255

train_labels = kr.utils.to_categorical(train_labels, constants.no_of_numbers)
test_label = kr.utils.to_categorical(test_label, constants.no_of_numbers)

# Creating a model and adding layers
# Sequential allows you to create a nerual network layer by layer
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