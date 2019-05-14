import csv
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
import glob
import random, os
import tkinter as tk
from tkinter import ttk
# from tkinter import *
from PIL import ImageTk, Image
import shutil

classifier = load_model('ankylosing_spondilitis_recognition.h5')
model_summary = classifier.summary()

names = [os.path.basename(x) for x in glob.glob('test_images\*.*')]
path = 'test_images\\'

with open('predictions.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect=csv.excel, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(["Filename",
                     "Keras"])

while True:
    random_filename = random.choice(os.listdir(path))
    random_file_path = path + random_filename

    if random_file_path is not None:
        test_image = image.load_img(random_file_path, target_size=(390, 215))
        test_image = image.img_to_array(test_image)
        test_image = test_image / 255
        test_image = np.expand_dims(test_image, axis=0)
        array = classifier.predict_proba(test_image)
        result = array[0]
        keras_prediction = np.argmax(result)
        tmp = [random_filename, keras_prediction]
        with open('predictions.csv', 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(list(tmp))
        shutil.move(random_file_path, 'D:\\Dropbox\\Sevcan\\avi-to-jpg-code\\tested')
    '''



    result = classifier.predict(test_image)
    training_set.class_indices
    if result[0][0] == 1:
        prediction = 'Exotropia'
    else:
        prediction = 'Esotropia'
    print (model_summary)
    print (prediction)
    '''
    else:


    src_file = os.path.join('D:\\Dropbox\Sevcan\\avi-to-jpg-code\\test_images\\predictions.csv')
    shutil.copy(src_file, 'D:\\Dropbox\\Sevcan\\avi-to-jpg-code\\tested')
    dst_file = os.path.join('D:\\Dropbox\\Sevcan\\avi-to-jpg-code\\test_images\\predictions.csv')
    os.rename(dst_file, 'Results.csv')
