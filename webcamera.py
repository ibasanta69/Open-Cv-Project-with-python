import cv2 as cp
cap = cp.VideoCapture(0, cp.CAP_DSHOW)
fourcc=cp.VideoWriter_fourcc(*"XVID")
ouput=cp.VideoWriter("basanta.avi",fourcc,20.0,(640,480))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cp.resize(frame, (400, 300))
     
        gray = cp.cvtColor(frame, cp.COLOR_BGR2GRAY)
        gray=cp.flip(gray,-1)
        ouput.write(gray)
        cp.imshow('Capture Camera', frame)
        cp.imshow('Gray', gray)
        print(cap.get(cp.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cp.CAP_PROP_FRAME_WIDTH))
       
        if cp.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
ouput.release()
cp.destroyAllWindows()
