import cv2 as cp
cout=0
cap=cp.VideoCapture('C:\\Users\\Death Empire\\Documents\\Bandicam\\ki.mp4')
ret,image=cap.read()
while True:
    if ret==True:
        cp.imwrite('C:\\Users\\Death Empire\\Documents\\Bandicam\\imN%d.jpg'%cout,image)
        cap.set(cp.CAP_PROP_POS_MSEC,(cout**100))
        ret,image=cap.read()
        cp.imshow('Video',image)
        cout+=1
        if cp.waitKey(1) & 0xFF==ord('q'):
            break
            cp.destroyAllWindows()
cap.release()
cp.destroyAllWindows()