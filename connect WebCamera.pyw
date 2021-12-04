import cv2 as cp
cap = cp.VideoCapture(0, cp.CAP_DSHOW)
print('vide', cap)
fourcc = cp.VideoWriter_fourcc(*"XVID")  # DIVX XVID MJPG WMVI WMV2
output = cp.VideoWriter("ou.avi", fourcc, 20.0, (640, 480))
#output = cp.VideoWriter("output.avi",fourcc,20.0,(640,480))
while (cap.isOpened()):
    ret, frame = cap.read()
    # frame=cp.resize(frame,(600,450))
    if ret == True:
        gray = cp.cvtColor(frame, cp.COLOR_BGR2GRAY)
        gray = cp.flip(gray, -0)
        cp.imshow('WebCam Camera', frame)
        cp.imshow('duplicat', gray)
        output.write(frame)
        if cp.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Npow capture video from webcame and save into memory
cap.release()
output.release()
cp.destroyAllWindows()
