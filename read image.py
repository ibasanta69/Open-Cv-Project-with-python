# read a image in open-cv
import cv2 as cp
img=cp.imread('g.jpg')
img=cp.resize(img,(400,600))
cp.imshow('image',img)
cp.waitKey()
cp.destroyAllWindows()
