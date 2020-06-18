import numpy as np
import cv2
print (np.version.version)
#pip install matplotlib==3.0.3
#pip install numpy==1.18.5
#pip install opencv-python == 4.2.0.34

# Read the main image
img_rgb = cv2.imread('q.jpg')
# Convert it to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# Read the template
template = cv2.imread('mark.png',0)
# Store width and heigth of template in w and h
w, h = template.shape[::-1]
# Perform match operations.
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
# Specify a threshold
threshold = 0.8
# Store the coordinates of matched area in a numpy array
loc = np.where( res >= threshold)
x=loc[0]
y=loc[1]
# Draw a rectangle around the matched region.
if len(x) and len(y):
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        # Show the final image with the matched area.
    #cv2.imshow('Detected',img_rgb)
    cv2.imwrite("test_001.png", img_rgb)
    print("I found the watermark")
else:
    print('there is no watermark')