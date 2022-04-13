# -*- coding: utf-8 -*-

import random

import cv2

import time

import sys

face_k = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

smile_k = cv2.CascadeClassifier("haarcascade_smile.xml")

video = cv2.VideoCapture(0)

numeric = 0

datas = cv2.LINE_AA

reng = (255,0,0)
 

 

def smile_detection(f_1,x1,y1):
    
    global numeric
    
    if numeric > 5000:
        
        x=str(random.randint(0,100))
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        color = (255,0,0)
        
        text = cv2.putText(f_1,"you smile is",(int(x1)+15,
                                               int(y1)-70),
                                               font,1,color,4,datas)
        
        text = cv2.putText(f_1,x +" %",(int(x1)+50,
                                        int(y1)-20),font,1,
                                        color,4,datas)
        
        time.sleep(15)
        
        numeric = 0
        
        return numeric

    else:
        x= str(random.randint(0,100))
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        color = (255,255,0)
        
        text = cv2.putText(f_1,"Smile Percent",(int(x1)+15,
                                                int(y1)-70),
                                                font, 1,
                                                color, 4, datas)
        
        
        text = cv2.putText(f_1, x+" %",(int(x1)+50,
                                        int(y1)-20),
                                        font, 1,
                                        color, 4,
                                        datas)
        
        numeric += 5
        
        return numeric



while True:
    
    check,f_1 = video.read()
    
    gray = cv2.cvtColor(f_1,cv2.COLOR_BGR2GRAY)
    
    face = face_k.detectMultiScale(gray,scaleFactor = 1.1,
                                   minNeighbors = 5)

    for x,y,w,h in face:
        img = cv2.rectangle(f_1,(x,y),
                            (x+(w+20),
                             y+(h-300)),
                             reng , -1)
        
        smiler = smile_k.detectMultiScale(gray,
                                          scaleFactor = 1.8,
                                          minNeighbors = 20)

        for x1,y1,w1,h1 in smiler:
            img = cv2.rectangle(f_1,(x1,y1),
                                (x1+(w1),
                                 y1+(h1)),
                                 reng , 3)
            
            smile_detection(f_1,x,y)
            

    cv2.imshow("Smiles",f_1)
    
    key = cv2.waitKey(1)
    
    if key  == ord('e'):
        
        break


video.release()

cv2.destroyAllWindows
