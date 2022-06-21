#-----Use VideoCapture in OpenCV-----
import cv2
import dlib
import math
from functions import *
from morse_converter import converter
BLINK_RATIO_THRESHOLD = 5.4

#-----livestream from the webcam----- 
cap = cv2.VideoCapture(0)

'''in case of a video
cap = cv2.VideoCapture("__path_of_the_video__")'''

#-----name of the display window in OpenCV-----
cv2.namedWindow('DECODE')

#-----Face detection with dlib-----
detector = dlib.get_frontal_face_detector()

#-----Detecting Eyes using landmarks in dlib-----
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
#-----these landmarks are based on the image above-----
left_eye_landmarks  = [36, 37, 38, 39, 40, 41]
right_eye_landmarks = [42, 43, 44, 45, 46, 47]

flag=0
s=''
duration=''

while True:
    #-----capturing frame-----
    retval, frame = cap.read()

    #-----exit the application if frame not found-----
    if not retval:
        print("Can't receive frame (stream end?). Exiting ...")
        break 

    #-----converting image to grayscale-----
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #-----Face detection with dlib-----
    #detecting faces in the frame 
    faces,_,_ = detector.run(image = frame, upsample_num_times = 0, 
                       adjust_threshold = 0.0)

    #-----Detecting Eyes using landmarks in dlib-----
    for face in faces:
        
        landmarks = predictor(frame, face)

        #-----Calculating blink ratio for one eye-----
        left_eye_ratio  = get_blink_ratio(left_eye_landmarks, landmarks)
        right_eye_ratio = get_blink_ratio(right_eye_landmarks, landmarks)
        blink_ratio     = (left_eye_ratio + right_eye_ratio) / 2
        
        if blink_ratio > BLINK_RATIO_THRESHOLD:
            #-----Blink detected!-----
            fl=f'{flag}'
            cv2.putText(frame,fl,(10,50), cv2.FONT_HERSHEY_SIMPLEX,
                       2,(255,255,255),2,cv2.LINE_AA)
            flag+=1
        else: 
            #-----detect if dot or dash-----
            if flag>15 and flag<=30:
                s+='.'                
            if flag>30 and flag<=50:
                s+='-' 
            if flag>5 and flag<=15:
                s+=' '
            flag=0
        
        cv2.putText(frame,s,(10,100), cv2.FONT_HERSHEY_SIMPLEX,
                        2,(255,255,255),2,cv2.LINE_AA)
        cv2.putText(frame,converter(s),(10,150), cv2.FONT_HERSHEY_SIMPLEX,
                        2,(255,255,255),2,cv2.LINE_AA)

    cv2.imshow('DECODE', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

#-----releasing the VideoCapture object-----
cap.release()
cv2.destroyAllWindows()