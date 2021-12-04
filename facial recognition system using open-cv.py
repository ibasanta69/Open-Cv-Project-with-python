from genericpath import isfile
import cv2 as cp
import numpy as np
from os import listdir
from os.path import isfile,join
data_path='C:/Users/Death Empire/Desktop/g/'
onlyfiles=[f for f in listdir(data_path) if isfile(join(data_path,f))]
training_data,Labels=[],[]
for i ,files in  enumerate(onlyfiles):
    image_path=data_path+onlyfiles[i]
    images=cp.imread(image_path,0)
    training_data.append(np.asarray(images,dtype=np.uint8))
    Labels.append(i)
Labels=np.asarray(Labels,dtype=np.int32)

model=cp.face.LBPHFaceRecognizer_create()
model.train(np.asarray(training_data),np.asarray(Labels))
print('Model Trainging complete !!')
