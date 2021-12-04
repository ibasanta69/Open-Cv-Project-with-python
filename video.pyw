import cv2
camera="http://192.168.1.11:8080/video"
cap = cv2.VideoCapture(0)
cap.open(camera)
print('cap', cap)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
ouput=cv2.VideoWriter('C:\\Users\\Death Empire\\Desktop\\outing.mp4v',fourcc,20.0,(600,450))
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame=cv2.resize(frame,(750,450))
        cv2.imshow('video', frame)
       # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # color dosplay video
       # gray=cv2.flip(gray,0)
       # cv2.imshow('frame', gray)
       # gray=cv2.flip(gray,0)
        ouput.write(frame)
        if cv2.waitKey(1)& 0xFF==ord('q'):
           break
cap.release()
ouput.release()
cv2.destroyAllWindows()
