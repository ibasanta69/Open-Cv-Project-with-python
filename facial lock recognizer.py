from genericpath import isfile

import cv2 as cp
import numpy as np
from os import listdir
from os.path import isfile, join
import datetime
import pyttsx3


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 160)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    print(audio)
    engine.runAndWait()


data_path = 'C:/Users/Death Empire/Desktop/g/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
training_data, Labels = [], []
for i, files in enumerate(onlyfiles):
    image_path = data_path+onlyfiles[i]
    images = cp.imread(image_path, 0)
    training_data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
Labels = np.asarray(Labels, dtype=np.int32)

model = cp.face.LBPHFaceRecognizer_create()
model.train(np.asarray(training_data), np.asarray(Labels))
print('Model Trainging complete !!')

face_classifier = cp.CascadeClassifier(
    'C:/Users/Death Empire/AppData/Local/Programs/Python/Python39/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def face_dector(img, size=0.5):
    gray = cp.cvtColor(img, cp.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return img, []
    for(x, y, w, h) in faces:
        cp.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 3)
        roi = img[y:y+h, x:x+w]
        roi = cp.resize(roi, (200, 300))
    return img, roi


#cap = cp.VideoCapture(0, cp.CAP_DSHOW)
# camera="http://192.168.1.11:8080/video"
cap = cp.VideoCapture(0, cp.CAP_DSHOW)
# cap.open(camera)
while(cap.isOpened()):
    ret, frame = cap.read()
    # frame=cp.resize(frame,(900,500))
    image, face = face_dector(frame)

    try:
        face = cp.cvtColor(face, cp.COLOR_BGR2GRAY)
        result = model.predict(face)
        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            display = str(confidence)+'% Basanta '
        datee = ('Date : '+str(datetime.datetime.now()))
        cp.putText(image, datee, (10, 40), cp.FONT_HERSHEY_COMPLEX_SMALL,
                   1, (255, 20, 147), 1, cp.LINE_AA)
        cp.putText(image, display, (200, 120),
                   cp.FONT_HERSHEY_COMPLEX, 1, (252, 186, 3), 2)

        if confidence > 75:

            datee = ('Date : '+str(datetime.datetime.now()))
            cp.putText(image, datee, (10, 40), cp.FONT_HERSHEY_COMPLEX_SMALL,
                       1, (255, 20, 147), 1, cp.LINE_AA)
            cp.putText(image, '''Face Unlocked
                            WelCome TO Basanta
            ''', (210, 450),
                cp.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
            cp.imshow('Face', image)
            speak('Welcome To You !')
        else:
            datee = ('Date : '+str(datetime.datetime.now()))
            cp.putText(image, datee, (10, 40), cp.FONT_HERSHEY_COMPLEX_SMALL,
                       1, (255, 20, 147), 1, cp.LINE_AA)
            cp.putText(image, '''Face locked
                            Invalid User
            ''', (210, 450),
                cp.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cp.imshow('Face', image)
            speak('Invalid User Please try again !')

    except:
        datee = ('Date : '+str(datetime.datetime.now()))
        cp.putText(image, datee, (10, 40), cp.FONT_HERSHEY_COMPLEX_SMALL,
                   1, (255, 20, 147), 1, cp.LINE_AA)
        cp.putText(image, 'Face Not Found', (200, 450),
                   cp.FONT_HERSHEY_COMPLEX, 1, (17, 0, 255), 3)
        cp.imshow('Face', image)
        speak(' Face Is Not Found please try again !')
        pass
    if cp.waitKey(1) == ord('q'):
        break
cap.release()
cp.destroyAllWindows()
