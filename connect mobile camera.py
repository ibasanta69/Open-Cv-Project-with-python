import cv2 as cp
camera="http://192.168.1.11:8080/video"
cap=cp.VideoCapture(0,cp.CAP_DSHOW)
cap.open(camera)
fourcc=cp.VideoWriter_fourcc(*"XVID")
output = cp.VideoWriter("outt.avi", fourcc, 20.0, (640, 480))
print('camera',cap.isOpened())
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        frame=cp.resize(frame,(400,300))
        cp.imshow('mobile Camera',frame)
        output.write(frame)
        if cp.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
output.release()
cp.destroyAllWindows()
