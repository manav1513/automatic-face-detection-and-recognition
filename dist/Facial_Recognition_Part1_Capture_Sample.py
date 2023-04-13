import cv2
import numpy as np
from playsound import playsound 
# c=conn.cursor()
# uid = c.lastrowid

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return None

    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]
    return cropped_face

cap = cv2.VideoCapture(0)
count = 0
while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count+=1
        crop1 = face_extractor(frame)
        face = cv2.resize(crop1,(120,120))
        # face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        file_name_path = 'DataSet/user'+str(count)+'.jpg'     #Dataset/user4.jpg
        # file_name_path1 = 'DataSet/frame'+str(count)+'.jpg'
        # print(file_name_path)
        # print(file_name_path1)

        cv2.imwrite(file_name_path,face)
        # cv2.imwrite(file_name_path1,frame)

        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow('Face Cropper',face)
    else:
        print("Face not Found")
        pass

    if cv2.waitKey(200)==27 or count==50:
        break
playsound('sound.mp3')
cap.release()
cv2.destroyAllWindows()
print('Collecting Samples Completed!!!')