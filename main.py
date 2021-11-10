from deepface import DeepFace
import shutil , os
import cv2
import numpy as np
import glob
from deepface.commons import functions



# def Detections():
#     for file in glob.glob("D:/2ndcomp/Edrive/New folder/image/*.jpg"):
#         img1 = cv2.imread('img.jpg')
#         img2 = cv2.imread(file)
#         df = DeepFace.verify(img1_path=img1, img2_path=img2)
#         print(df)
#         if df['verified']:
#             print("matched")
#         else:
#             print("not matching")
# Detections()


for file in glob.glob("D:/2ndcomp/Edrive/New folder/image/*.*"):
    img1 ='w3.jpg'
    df = DeepFace.verify(img1_path=img1, img2_path=file)
    print(df)
    if df['verified']:
        print("matched")
    else:
        print("not matching")
