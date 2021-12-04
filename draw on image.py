import numpy as np
import cv2 as cp
img = cp.imread('C:\\Users\\Death Empire\\Downloads\\g.jpg')
img = cp.resize(img, (550, 700))
# img=np.zeros([555,555,3],np.uint8)*255 black image create
#img = np.ones([555, 555, 3], np.uint8)*255  # create white image in numpy
img = cp.line(img, (90, 0), (200, 200), (184, 134, 11), 3)
img = cp.arrowedLine(img, (0, 125), (225, 255), (0, 255, 255), 4)
img = cp.rectangle(img, (24, 10), (333, 333), (0, 255, 255), 3)
img = cp.circle(img, (447, 125), 63, (0, 255, 255), 6)
img = cp.putText(img, 'Girl', (20, 500), cp.FONT_ITALIC,
                 4, (0, 255, 255), 10, cp.LINE_AA)
img = cp.ellipse(img, (400, 600), (100, 50), 10, 0, 270, 155, 5)
cp.imshow('imgae', img)
cp.waitKey()
cp.destroyAllWindows()
