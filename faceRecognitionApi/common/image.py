import numpy as np
import cv2
import os

cd = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(cd + '/../static/images/test.jpg')
print(img)