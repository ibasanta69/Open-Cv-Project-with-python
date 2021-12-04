# C:/Users/Death Empire/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml
import cv2 as cp
import numpy as np
face_classifier = cp.CascadeClassifier(
    'C:/Users/Death Empire/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def face_extract(img):
    gray = cp.cvtColor(img, cp.COLOR_BGR2GRAY)
    face = face_classifier.detectMultiScale(gray, 1.3, 5)
    if face is ():
        return None
    for(x, y, w, h) in face:
        crop_face = img[y:y+h, x:x+w]
    return crop_face


cap = cp.VideoCapture(0, cp.CAP_DSHOW)
count = 0
while True:
    ret, frame = cap.read()
    if (face_extract(frame)) is not None:
        count += 1
        faces = cp.resize(face_extract(frame), (200, 200))
        faces = cp.cvtColor(faces, cp.COLOR_BGR2GRAY)

        file_path = 'C:\\Users\\Death Empire\\Desktop\\g\\hook'+str(count)+'.jpg'
        cp.imwrite(file_path, faces)
        cp.putText(faces, str(count), (50, 50),
                   cp.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
        cp.imshow('crp face', faces)
    else:
        print('Face Not Found')
        pass
    if cp.waitKey(1) == ord('q'):
        break
cap.release()
cp.destroyAllWindows()
print('collecting samples complete')
