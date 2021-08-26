import cv2
import numpy as np
from .box import Box
from .train import *
from .config import model_path
import os
import pickle

def predict(img):
    path = os.path.join(model_path, "nn_trained_model_hog.sav")

    if not os.path.exists(path):
        print('Please wait while training the NN-HOG model....')
        train('NN', 'hog', 'nn_trained_model_hog')

    model = pickle.load(open(path, 'rb'))
    features = extract_features(img, 'hog')
    labels = model.predict([features])

    return labels


# if __name__ == "__main__":
#     img = cv2.imread('testresult/0_6.png')
#     labels = predict(img)
#     print(labels)
