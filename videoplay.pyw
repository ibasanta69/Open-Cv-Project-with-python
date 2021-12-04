import cv2 as cp
cap=cp.VideoCapture('C:\\Users\\Death Empire\Documents\\Bandicam\\ki.mp4')
print('video',cap)
while True:
    ret,frame=cap.read()
    frame=cp.resize(frame,(300,240))
    gray=cp.cvtColor(frame,cp.COLOR_BGR2GRAY)
    cp.imshow('original video',frame)
    cp.imshow('gray',gray)
    if cp.waitKey(100) & 0xFF==ord('q'):
        break
cap.release()
cp.destroyAllWindows()