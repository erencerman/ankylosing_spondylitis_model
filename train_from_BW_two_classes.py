from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import os
import cv2
from keras.models import model_from_json

# select the class number
classes_num = 2

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(64, (3, 3), input_shape=(150, 600, 1), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))


# Adding a second convolutional layer
classifier.add(Conv2D(64, (3, 3), activation='relu'))

# Adding a third convolutional layer
classifier.add(Conv2D(128, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Dropout(0.5))
# Adding a fourth convolutional layer
classifier.add(Conv2D(64, (3, 3), activation='relu'))

# Adding a fifth convolutional layer
classifier.add(Conv2D(32, (2, 2), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(3, 3)))

# Step 3 - Flattening
classifier.add(Flatten())
classifier.add(Dense(256, activation='relu'))
classifier.add(Dropout(0.5))
# one more dense layer may be added
#classifier.add(Dense(4096, activation='relu'))
#classifier.add(Dropout(0.5))

# Step 4 - Full connection
classifier.add(Dense(classes_num, activation='softmax'))


# Compiling the CNN
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Part 2 - Fitting the CNN to the images

train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory('D:\\Dropbox\\Sevcan\\avi-to-jpg-code\\dataset_second\\training_set', target_size=(150, 600),color_mode="grayscale", batch_size = 20, class_mode='categorical')
test_set = test_datagen.flow_from_directory('D:\\Dropbox\\Sevcan\\avi-to-jpg-code\\dataset_second\\test_set', target_size=(150, 600),color_mode="grayscale", batch_size=20, class_mode='categorical')
classifier.fit_generator(training_set, steps_per_epoch=800, epochs=16, validation_data=test_set, validation_steps=1000)

# This s what I have added. Saving  the model:
model_summary = classifier.summary()
classifier.save('AS_model_CHOROID-wider1.h5')

# Part 3 - Making new predictions

'''test_image = image.load_img('dataset/single_prediction/test.jpg', target_size=(300, 600))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
training_set.class_indices
array = classifier.predict(test_image)
result = array[0]

answer = np.argmax(result)
if answer == 1:
    print("Predicted:Exotropia")
else answer == 0:
    print("Predicted: Esotropia")'''
