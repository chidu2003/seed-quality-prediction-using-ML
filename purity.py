from keras.layers.normalization import layer_normalization
import tensorflow
import keras
from tensorflow.keras.models import Sequential
#from tensorflow import keras
import cv2
import matplotlib.pyplot as plt
import  numpy as np

from skimage.feature import peak_local_max
#from skimage.morphology import watershed
from scipy import ndimage
# load the image and perform pyramid mean shift filtering
# to aid the thresholding step
#nimage = cv2.imread(r"C:\Users\prana\OneDrive\Desktop\watershed\filewater_21.jpeg", cv2.IMREAD_GRAYSCALE)
SIZE = 120
model = keras.models.load_model('model\model.h5')
categories = ["broken", "discolored", "pure"]

image = cv2.imread(r"C:\Users\prana\OneDrive\Desktop\watershed\corn2.jpeg")
shifted = cv2.pyrMeanShiftFiltering(image, 21, 51)

# convert the mean shift image to grayscale, then apply
# Otsu's thresholding
gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
pure=0
tot_seeds=0
for (i, c) in enumerate(cnts):
    # draw the contour
    (x, y, w, h) = cv2.boundingRect(c)
    if(cv2.contourArea(c)>10.0 and cv2.arcLength(c,True)>200.0):
        tot_seeds=tot_seeds+1
        print("total= ",tot_seeds)
        nimage = image[y:y + h, x:x + w]
        pimage = cv2.resize(nimage,(SIZE,SIZE))
        pimage = pimage/255.0
        prediction = model.predict(np.array(pimage).reshape(-1,SIZE,SIZE,1))
        pclass = np.argmax(prediction)
        print("class= ",pclass)
        if(pclass=="2"):
            pure=pure+1
'''
plt.imshow(image)
pValue = "Prediction: {}".format((pure/tot_seeds)*100)
plt.title(pure)
realvalue = "Real Value 1"
plt.figtext(0,0,realvalue)
plt.show()

'''

'''import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
import tensorflow as tf
from model import createModel


def predict(SIZE):
    categories = ["NonDemented", "MildDemented", "ModerateDemented", "VeryMildDemented"]

    path = "./test/"
    images = []
    for img in os.listdir(path):
        data = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        new_data = cv2.resize(data, (SIZE, SIZE))
        new_data = new_data / 255.0
        images.append(new_data)
    model = createModel()
    title = os.listdir('./test')
    x = 0
    for img ,indx,value in images,enumerate(title):
        image = np.array(img).reshape(-1, SIZE, SIZE, 1)
        prediction = model.predict(image)
        plt.imshow(img, cmap="gray")
        ptitle = "Prediction: {0}".format(categories[np.argmax(prediction)])

        plt.figtext(0, 0, title[indx])
        plt.title(ptitle)
        plt.show()
        print(prediction)


    print(len(images), len(title))


predict(120)
'''
