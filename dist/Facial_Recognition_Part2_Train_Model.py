import cv2
import numpy as np
from os import listdir
# from os.path import isfile, join
from playsound import playsound

data_path = 'DataSet/'
onlyFiles = [f for f in listdir(data_path)]
print(onlyFiles)

Training_Data= []
Labels  = []

for i, files in enumerate(onlyFiles):
    image_path = data_path + onlyFiles[i]
    print(image_path)
    images = cv2.imread(image_path)
    cv2.imshow('Train to Dataset', images)
    cv2.waitKey(100)

    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    Training_Data.append(np.asarray(images, dtype=np.uint8))
    # print(Training_Data)
    Labels.append(i)
    # print(Labels)

Labels = np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(Training_Data), np.asarray(Labels))

playsound('model_trained.mp3')
print("Model Training Complete!!!!!")


