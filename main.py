import numpy as np
import cv2
import datetime
import os

drawing = False

def nothing(x):
    pass

def draw_circle(event, x, y, flags, param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            size = cv2.getTrackbarPos('Size', 'Brush Size')
            r = cv2.getTrackbarPos('R', 'Choose Color')
            g = cv2.getTrackbarPos('G', 'Choose Color')
            b = cv2.getTrackbarPos('B', 'Choose Color')

            cv2.circle(canvas, (x, y), size, (b, g, r), -1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

img_color = np.zeros((300, 370, 3), np.uint8)
cv2.namedWindow('Choose Color')

cv2.createTrackbar('R', 'Choose Color', 0, 255, nothing)
cv2.createTrackbar('G', 'Choose Color', 0, 255, nothing)
cv2.createTrackbar('B', 'Choose Color', 0, 255, nothing)

img_brush = np.zeros((300, 370, 3), np.uint8)
cv2.namedWindow('Brush Size')

cv2.createTrackbar('Size', 'Brush Size', 5, 100, nothing)

canvas = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Canvas. Press S to Save.')
cv2.setMouseCallback('Canvas. Press S to Save.', draw_circle)

while(1):
    if cv2.getWindowProperty('Choose Color', 1) == -1:
        break
    if cv2.getWindowProperty('Brush Size', 1) == -1:
        break
    if cv2.getWindowProperty('Canvas. Press S to Save.', 1) == -1:
        break

    cv2.imshow('Choose Color', img_color)
    cv2.imshow('Brush Size', img_brush)
    cv2.imshow('Canvas. Press S to Save.', canvas)

    k = cv2.waitKey(1)
    if k == ord('s'):
        currtime = datetime.datetime.now()
        currtime_str = currtime.strftime("%d-%m-%Y %I-%M-%S %p")
        filename = 'drawing/' + currtime_str + '.png'
        cv2.imwrite(filename, canvas)
        
    r = cv2.getTrackbarPos('R', 'Choose Color')
    g = cv2.getTrackbarPos('G', 'Choose Color')
    b = cv2.getTrackbarPos('B', 'Choose Color')

    img_color[:] = [b, g, r]

    size = cv2.getTrackbarPos('Size', 'Brush Size')
    img_brush[:] = 0
    cv2.circle(img_brush, (150, 135), size, (b, g, r), -1)

cv2.destroyAllWindows()