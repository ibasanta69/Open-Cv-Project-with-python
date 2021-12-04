import cv2 as cp
import numpy as np
# create mouse callback function


def draw(event, x, y, flags, param):
    print('x==',x)
    print('y==',y)
    print('flags',flags)
    print('param',param)
    if event == cp.EVENT_LBUTTONDBLCLK:
        cp.circle(img,(x,y), 100, (125, 0, 255), 5)
    if event == cp.EVENT_RBUTTONDBLCLK:
        cp.rectangle(img, (x, y), (x+100, y+75), (124, 125, 255), 2)


cp.namedWindow(winname='result')
img = np.zeros((512, 512, 3), np.uint8)
cp.setMouseCallback('result', draw)
while True:
    cp.imshow('result', img)
    if cp.waitKey(1) & 0xFF == ord('q'):
        break
cp.destroyAllWindows()
